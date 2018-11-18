#coding=utf-8
# -*- coding: utf-8 -*-
import vk_api
import config
vk_session = vk_api.VkApi(config.login, config.password)
vk_session.auth()

vk = vk_session.get_api()


res = vk.market.getAlbums(
    owner_id='-'+config.groupId,
    count=100)

print(res)

# def deleteAlbum(id):
#     vk.market.deleteAlbum(
#         owner_id = '-'+config.groupId,
#         album_id = id
#     )

# for i in res['items']:
#     deleteAlbum(i['id']);
#     print('deleted',i['id'])