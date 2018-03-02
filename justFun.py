#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 15:33:33
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : 0.1

import os

import sys
import json
import urllib
import requests
import time
import re
from dao.saveToFile import *

class WebSpider(object):
    """docstring for getData
    """
    def __init__(self,URL_OPEN,URL_REQUEST,HEADERS,UID,SECRET):
        # super(DataCollector, self).__init__()
        self.URL_OPEN = URL_OPEN
        self.URL_REQUEST=URL_REQUEST
        self.UID=UID
        self.SECRET=SECRET

        self.s = requests.Session()

        # 加headers 伪造请求头。
        self.headers = HEADERS


    def get_csrf_token(self):
        """
        因为登录时需要先获取csrfToken值，所以先get获取，
        然后在下方post数据的时候使用。
        :return: csrfToken
        """
        res = self.s.get(self.URL_OPEN)
        print res.status_code
        # print page.cookies["censys.io.beaker.session.id"]
        cookie=res.cookies
        htmlText=res.text
        # print(htmlText)
        # <input type="hidden" name="csrf_token" value="7e5e35fd174fe55fc75dfeb6f01c5944f21e463b">
        # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
        pattern = re.compile(r'''<input type=.* name="csrf_token" value=(.*)>''')
        # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
        # 这个例子中使用match()无法成功匹配
        match = re.search(pattern,htmlText)
        if match:
            # 使用Match获得分组信息
            csrfToken=match.group(1)
            return (cookie,csrfToken)
        # csrfToken = page.cookies['CSRF_TOKEN']

    def login(self,paramsDatas,cookies):
        '''
        使用request方法，获取网页内容
        '''
        #res = self.s.post(self.URL_REQUEST,data=paramsDatas,cookies=cookies)
        res = self.s.post(self.URL_REQUEST,data=paramsDatas,headers=self.headers)
        cookie=res.cookies
        # print (res.status_code)
        # print res.cookies["censys.io.beaker.session.id"]
        # print (res.text)
        # res.encoding = 'GBK'
        # print(res.text,res.encoding)
        # res=json.loads(res.text)
        # res = res.json()
        # print res
        # print "job id is :"+res["job_id"]
        if res.status_code == 200  :
            print("The job was retreived successfully.")
            SaveToFile.saveToFileAsHtml("censyslogin.html",res.text)
            return cookie
        elif res.status_code == 404 :
            print("he specified job ID was invalid and could not be found.")
        elif  res.status_code == 429 :
            print("The requested record was not retrieved because you have exceeded your specified rate limit.")
        elif  res.status_code == 500 :
            print("""An unexpected error occurred when trying to execute your query.Try again at a later time or contact us at requests@censys.io if the problem persists.""")
        else:
            pass


    def getContentWithPost(self,contentURL,paramsDatas,cookies):
        '''
        使用request方法，获取网页内容
        '''

        res = self.s.post(contentURL,data=paramsDatas)
        if res.status_code == 200  :
            print("The job was retreived successfully.")
            # print res.text
            SaveToFile.saveToFileAsHtml("censys.html",res.text)
        elif res.status_code == 404 :
            print("he specified job ID was invalid and could not be found.")
        elif  res.status_code == 429 :
            print("The requested record was not retrieved because you have exceeded your specified rate limit.")
        elif  res.status_code == 500 :
            print("""An unexpected error occurred when trying to execute your query.Try again at a later time or contact us at requests@censys.io if the problem persists.""")
        else:
            pass


    def getContentWithGet(self):
        '''
        使用request方法，获取网页内容
        '''
        while True:
            res = self.s.get(self.URL_REQUEST, auth=(self.UID, self.SECRET))


    def getContentWithURLlib(self):
        '''
        使用urllib方法，获取网页内容
        '''

        #爬取结果
        response = urllib.urlopen(self.API_URL)

        data = response.read()

        # print data

        # 设置解码方式
        data = data.decode('utf-8')

        #打印结果
        print(data)

        #打印爬取网页的各类信息

        print(type(response))
        print(response.geturl())
        print(response.info())
        print(response.getcode())

if __name__ == "__main__":

    # API_URL = "http://www.china-longchen.com/"
    URL = "https://www.censys.io/login"
    UID = "a9cd377f-0144-4376-9820-d5cc25c9ce25"
    SECRET = "Suq8m700V3mFcxFZvtxa3nouIEvhWf2n"

    # paramsData={"query":"SELECT location.country, count(ip) FROM ipv4.20151020 GROUP BY location.country;"}

    Headers ={
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.8',
        'cookie':'_gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_day=1; _gauges_unique_hour=1; _gat=1; censys.io.beaker.session.id=86542fff711c3bd4a3414d73c8b9a61225b03272khUymgQ2F/NfRPHaP4P84l1gA9X5hKhwHv1+5ufn9phVBKMZ6DAu7LBCAYPJJBAl+5fOsgxuuTYU//X50GK0foL44mBjlKjeNDG7qVIhnDHjH+Pyd1uKRU+Y6YcGAP2JUiK+suQYoYfgYtN4V5l0wHNGQ1J62eX90GJz+3a/mV407ACf6o1SpPbFqGBbmyd+wFUhQ+odUShVRSudNuKSoOo/EK9BznAY73Yi8Qep/zOR5Zmpcc/Ayy1E2iVdJMDalDYXgoo9vOB0bTJ1vQKTA6hHSf8ctlRtMaM=; _ga=GA1.2.963336915.1503454419; _gid=GA1.2.2129058772.1504081111',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.25 Safari/537.36',
        'referer':URL
    }

    spider=WebSpider(URL,URL,Headers,UID,SECRET)
    cookie,csrf_token=spider.get_csrf_token()
    # print("cookie:"+str(cookie))
    print("csrf_token:"+csrf_token)
    params={
              "login":"jingquanliang",
              "password":"1qaz2wsx",
              "came_from":"/",
              "csrf_token":csrf_token
    }
    jsonParams=json.dumps(params)
    cookie=spider.login(jsonParams,cookie) #登录censys

    contentURL = "https://censys.io/query/export/ahZzfnN0ZWFkeS1jaXJjdWl0LTkxNDE3cjsLEhFCaWdRdWVyeUV4ZWN1dGlvbiIkODkxYjgzYWItOGQ0MS0xMWU3LWExZmItMjM0ZGFiNmU5YjA4DA"
    job_id=spider.getContentWithPost(contentURL,jsonParams,cookie)


