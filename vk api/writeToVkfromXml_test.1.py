#coding=utf-8
# -*- coding: utf-8 -*-
#https://vk.com/public173901748
import vk_api
import xmltodict
import json
import os,time,sys,argparse,datetime,re
import requests
import config

# def captcha_handler(captcha):
#     print('captcha')
#     print(captcha)
#,captcha_handler=captcha_handler

vk_session = vk_api.VkApi(config.login, config.password)
vk_session.auth()
vk = vk_session.get_api()

res = vk.photos.getMarketUploadServer(group_id=config.groupId,main_photo=1)
#print(res)
url = res['upload_url']
pathPhoto = 'c:\\myProject\\python\\vk api\\images\\'

with open('db\\index.xml') as fd:
    doc = xmltodict.parse(fd.read())

offer = doc['yml_catalog']['shop']['offers']['offer']

def loadFileUrl(fulllocalname):
    global vk
    headers = {'cache-control': "no-cache"}
    cookies = {}
    data = {}
    files = { 'file': open(fulllocalname, 'rb') }
    r = requests.post(url, headers=headers, cookies=cookies, data=data, files=files)
    r_obj = json.loads(r.text)
    if 'photo' in r_obj:
        resultSave = vk.photos.saveMarketPhoto(group_id=config.groupId,
            photo=r_obj['photo'],
            server = r_obj['server'],
            hash = r_obj['hash'],
            crop_data = r_obj['crop_data'],
            crop_hash = r_obj['crop_hash']
        )
        return resultSave[0]['id']
    else:
        return None
if os.path.isfile('db\\nodik_vk.db'):
    fileResult = open('db\\nodik_vk.db','r');
    loadingIds = [x.split('\t')[0] for x in fileResult.readlines()]
    fileResult.close()
else:
    loadingIds=[]
fileResult = open('db\\nodik_vk.db','a');
fileError = open('txt\\fileError.log','a');
count = len(loadingIds)
countAll = len(offer[2000:])
isWrite = False
isFerst=True
for i in offer[2000:]:
    isWrite= False
    if i['@id'] not in loadingIds:
        if 'picture' in i:
            filename = i['picture'].split('/')[-1]
            fulllocalname = pathPhoto + filename
            main_photo_id = loadFileUrl(fulllocalname)
            if not main_photo_id is None :
                if len(i['name'])>=4 and len(i['description'])>=10:
                    name = i['name'][0:80]
                    #fileResult.write(name)
                    #print(name)
                    try:
                        if isFerst:
                            captcha_sid='693745865982';
                            captcha_key='dcdsd';
                            isFerst=False
                        else:
                            captcha_sid=None;
                            captcha_key=None;
                        resm = vk.market.add(
                            owner_id='-'+config.groupId,
                            name = name,
                            description=i['description'],
                            category_id=305,
                            price=i['price'],
                            main_photo_id=main_photo_id,
                            captcha_sid=captcha_sid,
                            captcha_key=captcha_key
                        )
                    except vk_api.exceptions.Captcha as e:
                        print(e.get_url())
                        break
                        # captcha_img = e.error['captcha_img']
                        # captcha_sid = e.error['captcha_sid']
                        # print(captcha_img,captcha_sid)
                    fileResult.write(str(i['@id']) + '\t' + str(resm['market_item_id'])+'\n');
                    isWrite=True
                else:
                    fileError.write(i['@id']+ ' name < 4  or  -  description < 10 ' + '\n')
            else:
                fileError.write(i['@id']+ 'file not load to vk - ' + fulllocalname + '\n')
        else:
            fileError.write(i['@id']+ 'from site not image - ' + i['url'] + '\n')
        count = count + 1
        print(count,'\t',count/countAll*100,'%',isWrite)