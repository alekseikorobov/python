#coding=utf-8
# -*- coding: utf-8 -*-
import vk_api
import config

vk_session = vk_api.VkApi(config.login, config.password)
vk_session.auth()

vk = vk_session.get_api()

print(vk.market.getCategories(count=1000))
print(vk.market.getCategories(count=1000,offset=1000))

#print(vk.photos.getMarketUploadServer(group_id='173901748'))