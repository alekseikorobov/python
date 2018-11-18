#coding=utf-8
# -*- coding: utf-8 -*-
import vk_api
import config

def writeToFile(res):
    file = open("txt\\vk.txt","a+")
    for i in res['items']:
        t = str(i['title']);
        f = (str(i['id']) + u'\t' + t + u'\n')
        file.write(f)
    file.close()

vk_session = vk_api.VkApi(config.login, config.password)
vk_session.auth()

vk = vk_session.get_api()

offset=0
i=0;
res = vk.market.get(owner_id='-'+config.groupId,count=200,offset=offset)
count = len(res['items'])
print(count)
i = 0
while(count == 200):
    res = vk.market.get(owner_id='-'+config.groupId,count=200,offset=offset)
    count = len(res['items'])
    offset = offset + 200
    writeToFile(res)
    print(i,offset)
    i = i + 1

print('ok')