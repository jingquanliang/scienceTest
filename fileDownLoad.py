#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-31 12:16:57
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : $Id$

#下载网页文件到本地文件夹
import os,urllib2,urllib

#设置下载后存放的存储路径'C:\Users\yinyao\Desktop\Python code'
path=r'C:\Users\yinyao\Desktop\Python code'
# file_name=r'MSFT.csv'   #文件名，包含文件格式
# dest_dir=os.path.join(path,file_name)

#设置下载链接的路径
url="https://storage.googleapis.com/censys-bigquery-export/48cdd44f-3d61-4dff-910a-3d7cc43e687b-000000000000.json"


def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position


def readFile(dest_file):
    filePathList=[]
    file=open(dest_file)

    for line in file:
        print(line)
        filePathList.append(line)
    return filePathList

#定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
def downLoadPicFromURL(URL):
    filePathList=readFile("D:\PythonWorkSpace\scienceTest\censys.txt")
    # exit(1)
    for Url in filePathList:
        try:
            index=find_last(Url,"/")
            file_name=Url[index+1:-1]
            # print file_name
            urllib.urlretrieve(Url , os.path.join(path,file_name))
        except:
          print '\tError retrieving the URL:', Url

#运行
downLoadPicFromURL(url)
