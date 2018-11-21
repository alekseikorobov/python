#coding=utf-8
# -*- coding: utf-8 -*-
import vk_api
import const
import config

vk_session = vk_api.VkApi(config.login, config.password)
vk_session.auth()

vk = vk_session.get_api()

l = list(set([const.list[x] for x in const.list]))
def createAlbom(name):
    res = vk.market.addAlbum(
        owner_id = '-'+config.groupId,
        title = name
    )
    return res['market_album_id']

vk_category = open('db\\vk_category.db','a+')
for i in l:
    if i != '':
        catVkId = createAlbom(i)
        print(catVkId)
        vk_category.write(i + '\t' + str(catVkId) + '\n')

print('ok')