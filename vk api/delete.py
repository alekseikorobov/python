
#coding=utf-8
# -*- coding: utf-8 -*-
#https://vk.com/public173901748
import vk_api
import json
import os,time,sys,argparse,datetime,re
import requests
import config

vk_session = vk_api.VkApi(config.login, config.password)
vk_session.auth()
vk = vk_session.get_api()

def delete(res):
    global vk
    for i in res['items']:
        res = vk.market.delete(
            owner_id='-'+config.groupId,
            item_id = i['id'])

offset=0
count = 200
i = 0
while(count == 200):
    res = vk.market.get(owner_id='-'+config.groupId,count=200,offset=offset)
    count = len(res['items'])
    offset = offset + count
    delete(res)
    print(i,offset)
    i = i + 1

print('ok')