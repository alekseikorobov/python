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

res = vk.photos.getMarketUploadServer(group_id=config.groupId,main_photo=1)
print(res)
url = res['upload_url']

#--- request

headers = {
    'cache-control': "no-cache",
}
cookies = {}
data = {}
files = {
    'file': open('c:\\myProject\\python\\vk api\\images\\B01712-500x500.jpeg', 'rb')
}

r = requests.post(url, headers=headers, cookies=cookies, data=data, files=files)
print('----------------')
print(r.text)
print('----------------')
#--- request end
r_obj = json.loads(r.text)
print(r_obj)
print('----------------')
json_data = r_obj['photo']
photo_obj = json.loads(json_data)
print(photo_obj)
print('----------------')
print(r_obj['hash'])
print('----------------')
print('----------------')

resultSave = vk.photos.saveMarketPhoto(group_id=config.groupId,
    photo=r_obj['photo'],
    server = r_obj['server'],
    hash = r_obj['hash'],
    crop_data = r_obj['crop_data'],
    crop_hash = r_obj['crop_hash']
)
print('resultSave')
print(resultSave)
print('----------------')
print('resultSave[0]')
print(resultSave[0]['id'])
print('----------------')
resm = vk.market.add(
    owner_id='-173901748',
    name='111111',
    description='111111111111',
    category_id=305,
    price=0.01,
    main_photo_id=resultSave[0]['id'],
)
print('resm')
print(resm)
print('----------------')
print('ok')