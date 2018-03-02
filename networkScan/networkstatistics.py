#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 15:33:33
# @Author  : Quanliang Jing (540692237@qq.com)
# @Link    : http://www.999own.com/
# @Version : 0.1

import os

import sys
import json
import requests

API_URL = "https://www.censys.io/api/v1"
UID = "a9cd377f-0144-4376-9820-d5cc25c9ce25"
SECRET = "Suq8m700V3mFcxFZvtxa3nouIEvhWf2n"

# paramsData={"query":"SELECT location.country, count(ip) FROM ipv4.20151020 GROUP BY location.country;"}
paramsData={
  "allowLargeResults": True,
  "query":"SELECT ip FROM ipv4.20170901;",
  "format":"json",
  "flatten":False
}
# print(json.dumps(paramsData)["query"])
res = requests.post(API_URL + "/export", auth=(UID, SECRET),data=json.dumps(paramsData))
print res.text
if res.status_code != 200:
    print "error occurred: %s" % res.status_code
    sys.exit(1)
else:
	print("create job success!")