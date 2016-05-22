#coding=utf-8

import urllib2
import re
import base64_codec
import subprocess
import xmltodict
import json
import time

# 获取 ishadowsocks 免费密码并生成配置文件

a_section = dict()
b_section = dict()
c_section = dict()

def get_middle_str(content,startStr,endStr):

    patternStr = r'%s(.+?)%s'%(startStr,endStr)

    p = re.compile(patternStr,re.IGNORECASE)

    foundallitems = re.findall(p,content)

    return foundallitems

def configIn(item):

    myItems = re.findall('<h4>.*?</h4>',item,re.S)

    isASection = False
    isBSection = False
    isCSection = False

    for item in myItems:

        if u'A服务器地址:' in item:

            isASection = True
            isBSection = False
            isCSection = False

            a_section['server'] = get_middle_str(item,u'A服务器地址:','</h4>')

        if u'B服务器地址:' in item:

            isASection = False
            isBSection = True
            isCSection = False

            b_section['server'] = get_middle_str(item,u'B服务器地址:','</h4>')

        if u'C服务器地址:' in item:

            isASection = False
            isBSection = False
            isCSection = True

            c_section['server'] = get_middle_str(item,u'C服务器地址:','</h4>')

        if u'端口:' in item:

            if isASection:

                a_section['server_port'] = get_middle_str(item,u'端口:','</h4>')

            elif isBSection:

                b_section['server_port'] = get_middle_str(item,u'端口:','</h4>')

            elif isCSection:

                c_section['server_port'] = get_middle_str(item,u'端口:','</h4>')

        if u'密码:' in item:

            if isASection:

                a_section['password'] = get_middle_str(item,u'密码:','</h4>')

            elif isBSection:

                b_section['password'] = get_middle_str(item,u'密码:','</h4>')

            elif isCSection:

                c_section['password'] = get_middle_str(item,u'密码:','</h4>')

        if u'加密方式:' in item:

            if isASection:

                a_section['method'] = get_middle_str(item,u'加密方式:','</h4>')

            elif isBSection:

                b_section['method'] = get_middle_str(item,u'加密方式:','</h4>')

            elif isCSection:

                c_section['method'] = get_middle_str(item,u'加密方式:','</h4>')

def encode_utf8(unicodestring):

    return str(unicodestring[0]).encode("utf-8")

def GetPage(myUrl):

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(myUrl, headers = headers)
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()
    #encode的作用是将unicode编码转换成其他编码的字符串
    #decode的作用是将其他编码的字符串转换成unicode编码
    unicodePage = myPage.decode("utf-8")

    # 找出所有class="content"的div标记
    #re.S是任意匹配模式，也就是.可以匹配换行符
    myItems = re.findall('<div class="col-lg-4 text-center">.*?</div>',unicodePage,re.S)
    items = []
    for item in myItems:

        if u'服务器地址' in item:

            configIn(item)

    print(a_section)
    print(b_section)
    print(c_section)

    base64string(b_section)

def base64string(config_info):

    base64string = encode_utf8(config_info['method']) + ':' + encode_utf8(config_info['password']) + '@' + encode_utf8(config_info['server']) + ':' + encode_utf8(config_info['server_port'])

    finalurl = 'ss://' + str(base64_codec.base64_encode(base64string)[0])

    print(finalurl)

# 获取 获取 ishadowsocks for mac plist 文件，进行解析和重新生成

def replace(list = [],index = 0,info = ''):

    list.remove(list[index])
    list.insert(index,encode_utf8(info).decode("utf-8"))
    return list

def update_plist_file_with(config_info):

    item_a = '{"current":0,"profiles":[{"password":"'+ config_info['password'][0] +'","method":"'+ config_info['method'][0] +'","server_port":'+ config_info['server_port'][0] +',"remarks":"","server":"'+ config_info['server'][0] +'"}]}'

    data_value = str(base64_codec.base64_encode(item_a)[0]).decode("utf-8")

    result_value = r'<?xml version="1.0" encoding="UTF-8"?>*<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">*<plist version="1.0">*<dict>*<key>PBS</key>*<string>Copv9p5PRHLeK66opkTUkg/nOAlBLd9A3+659k/x3nUmz2O1HoVxtuxOjhRzVzNG</string>*<key>ShadowsocksIsRunning</key>*<false/>*<key>ShadowsocksMode</key>*<string>auto</string>*<key>config</key>*<data>*%s</data>*<key>proxy encryption</key>*<string>%s</string>*<key>proxy ip</key>*<string>%s</string>*<key>proxy password</key>*<string>%s</string>*<key>proxy port</key>*<string>%s</string>*<key>public server</key>*<false/>*</dict>*</plist>'%(data_value,config_info['method'][0],config_info['server'][0],config_info['password'][0],config_info['server_port'][0])

    list = result_value.split('*')

    file_name = 'temp_' + str(time.time()) + '.plist'

    with open(file_name, "w+") as f:

        for item in list:

            f.write(str(item) + "\n")

    export_setting = "plutil -convert binary1 " + file_name

    subprocess.Popen(export_setting, shell=True).wait()

    replace_setting = "mv " + file_name +" ~/Library/Preferences/clowwindy.ShadowsocksX.plist"

    subprocess.Popen(replace_setting, shell=True).wait()

# 主函数
def main():

    GetPage('http://www.ishadowsocks.net/')

    # finalurl = str(base64_codec.base64_decode('eyJjdXJyZW50IjoxLCJwcm9maWxlcyI6W3sicGFzc3dvcmQiOiI0MDE3MDcwNSIsIm1ldGhvZCI6ImFlcy0yNTYtY2ZiIiwic2VydmVyX3BvcnQiOjQ0MywicmVtYXJrcyI6IiIsInNlcnZlciI6InVzMS5pc3MudGYifSx7InBhc3N3b3JkIjoiODEyMDI5NTkiLCJtZXRob2QiOiJhZXMtMjU2LWNmYiIsInNlcnZlcl9wb3J0Ijo0NDMsInJlbWFya3MiOiIiLCJzZXJ2ZXIiOiJ1czEuaXNzLnRmIn1dfQ==')[0])

    # print(finalurl)

    update_plist_file_with(a_section)

if __name__ == '__main__':
  main()