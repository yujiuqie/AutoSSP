#coding=utf-8

import urllib2
import re

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


# 主函数
def main():

    GetPage('http://www.ishadowsocks.net/')

if __name__ == '__main__':
  main()