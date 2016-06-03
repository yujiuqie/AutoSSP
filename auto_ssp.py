# coding=utf-8

# Created by Alfred Jiang 20160523

import urllib2
import re
import base64_codec
import subprocess
import time

# 网络爬虫
# 正则表达式
# 字符编码
# 文件操作
# plist - plutil
# 执行 shell 脚本

# 获取 ishadowsocks 免费密码并更新配置文件

a_section = dict()
b_section = dict()
c_section = dict()


def get_middle_str(content, start_str, end_str):
    
    pattern_str = r'%s(.+?)%s' % (start_str, end_str)

    p = re.compile(pattern_str, re.IGNORECASE)

    found_all_items = re.findall(p, content)

    return found_all_items


def generate_configuration_file(item):
    
    my_items = re.findall('<h4>.*?</h4>', item, re.S)

    is_a_section = False
    is_b_section = False
    is_c_section = False

    for item in my_items:

        if u'A服务器地址:' in item:

            is_a_section = True
            is_b_section = False
            is_c_section = False

            a_section['server'] = get_middle_str(item, u'A服务器地址:', '</h4>')

        if u'B服务器地址:' in item:

            is_a_section = False
            is_b_section = True
            is_c_section = False

            b_section['server'] = get_middle_str(item, u'B服务器地址:', '</h4>')

        if u'C服务器地址:' in item:

            is_a_section = False
            is_b_section = False
            is_c_section = True

            c_section['server'] = get_middle_str(item, u'C服务器地址:', '</h4>')

        if u'端口:' in item:

            if is_a_section:

                a_section['server_port'] = get_middle_str(item, u'端口:', '</h4>')

            elif is_b_section:

                b_section['server_port'] = get_middle_str(item, u'端口:', '</h4>')

            elif is_c_section:

                c_section['server_port'] = get_middle_str(item, u'端口:', '</h4>')

        if u'密码:' in item:

            if is_a_section:

                a_section['password'] = get_middle_str(item, u'密码:', '</h4>')

            elif is_b_section:

                b_section['password'] = get_middle_str(item, u'密码:', '</h4>')

            elif is_c_section:

                c_section['password'] = get_middle_str(item, u'密码:', '</h4>')

        if u'加密方式:' in item:

            if is_a_section:

                a_section['method'] = get_middle_str(item, u'加密方式:', '</h4>')

            elif is_b_section:

                b_section['method'] = get_middle_str(item, u'加密方式:', '</h4>')

            elif is_c_section:

                c_section['method'] = get_middle_str(item, u'加密方式:', '</h4>')


def fetch_free_config_info(info_url):
    
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

    headers = {'User-Agent': user_agent}

    req = urllib2.Request(info_url, headers=headers)

    info_response = urllib2.urlopen(req)

    config_info = info_response.read()

    unicode_info = config_info.decode("utf-8")

    config_items = re.findall('<div class="col-lg-4 text-center">.*?</div>', unicode_info, re.S)

    for item in config_items:

        if u'服务器地址' in item:

            generate_configuration_file(item)


def encode_utf8(unicodestring):
    
    return str(unicodestring[0]).encode("utf-8")


def print_qr_code_info(config_info):

    base64string = encode_utf8(config_info['method']) \
                   + ':' \
                   + encode_utf8(config_info['password']) \
                   + '@' \
                   + encode_utf8(config_info['server']) \
                   + ':' \
                   + encode_utf8(config_info['server_port'])

    finalurl = 'ss://' + str(base64_codec.base64_encode(base64string)[0])

    print(finalurl)


def generate_new_data(config_info):

    # export_setting = "plutil -convert xml1 ~/Library/Preferences/clowwindy.ShadowsocksX.plist -o clowwindy.ShadowsocksX.plist.xml"
    # subprocess.Popen(export_setting, shell=True).wait()
    #
    # with open('clowwindy.ShadowsocksX.plist.xml') as fd:
    #     doc = xmltodict.parse(fd.read())
    #
    # current_profile_info = base64_codec.base64_decode(str(doc['plist']['dict']['data']))

    start_config_string = '{"current":0,"profiles":['

    mid_config_string = '{"password":"' \
                        + config_info['password'][0] \
                        + '","method":"' \
                        + config_info['method'][0] \
                        + '","server_port":' \
                        + config_info['server_port'][0] \
                        + ',"remarks":"","server":"' \
                        + config_info['server'][0] \
                        + '"}'

    end_config_string = ']}'

    full_config_string = start_config_string + mid_config_string + end_config_string

    data_value = base64_codec.base64_encode(full_config_string)

    return data_value[0]


def update_plist_file_with(config_info):

    data_value = generate_new_data(config_info)

    plist = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">',
        '<plist version="1.0">',
        '<dict>',
        '<key>PBS</key>',
        '<string>Copv9p5PRHLeK66opkTUkg/nOAlBLd9A3+659k/x3nUmz2O1HoVxtuxOjhRzVzNG</string>',
        '<key>ShadowsocksIsRunning</key>',
        '<false/>',
        '<key>ShadowsocksMode</key>',
        '<string>auto</string>',
        '<key>config</key>',
        '<data>',
        '' + data_value + '</data>',
        '<key>proxy encryption</key>',
        '<string>' + config_info.get('method')[0] + '</string>',
        '<key>proxy ip</key>',
        '<string>' + config_info.get('server')[0] + '</string>',
        '<key>proxy password</key>',
        '<string>' + config_info.get('password')[0] + '</string>',
        '<key>proxy port</key>',
        '<string>' + config_info.get('server_port')[0] + '</string>',
        '<key>public server</key>',
        '<false/>',
        '</dict>',
        '</plist>'
    ]

    file_name = 'temp_' + str(time.time()) + '.plist'

    with open(file_name, "w+") as f:
        for item in plist:
            f.write(str(item) + "\n")

    generate_binary_plist = "plutil -convert binary1 " + file_name

    subprocess.Popen(generate_binary_plist, shell=True).wait()

    import_new_plist = "defaults import clowwindy.ShadowsocksX " + file_name

    subprocess.Popen(import_new_plist, shell=True).wait()

    rm_temp_file = "rm " + file_name

    subprocess.Popen(rm_temp_file, shell=True).wait()


def fetch_a_section():

    fetch_section(a_section)


def fetch_b_section():

    fetch_section(b_section)


def fetch_c_section():

    fetch_section(c_section)


def fetch_section(section):

    fetch_free_config_info('http://www.ishadowsocks.net/')

    update_plist_file_with(section)

    print_qr_code_info(section)


# 主函数
def main():

    fetch_c_section()

    # fetch_free_config_info('http://www.ishadowsocks.net/')
    #
    # print_qr_code_info(b_section)
    #
    # update_plist_file_with(a_section)


if __name__ == '__main__':

    main()
