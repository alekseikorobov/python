# -*- coding: utf-8 -*-
import xmltodict,sys,const
import vk_api
import config

vk_session = vk_api.VkApi(config.login, config.password)
vk_session.auth()
vk = vk_session.get_api()


with open('db\\index.xml') as fd:
    doc = xmltodict.parse(fd.read())

category = doc['yml_catalog']['shop']['categories']['category']
offer = doc['yml_catalog']['shop']['offers']['offer']

listFromvk = open('txt\\vk.txt','r').readlines()

site_vk = open('db\\nodik_vk.db','r').readlines()
site_vk_list = [(x.split('\t')[0],x.split('\t')[1].replace('\n','')) for x in site_vk]
site_vk_d = dict(site_vk_list)

vk_category = open('db\\vk_category.db','r').readlines()
vk_category_list = [(x.split('\t')[0],x.split('\t')[1].replace('\n','')) for x in vk_category]
vk_category_d = dict(vk_category_list)

vkitemAlbum = open('db\\vkitemAlbum.db','r').readlines()
vkitemAlbum_list = [str(x.split(' ')[0]) for x in vkitemAlbum]
print(vkitemAlbum_list)
def getCatName(catId):
    for i in category:
        if catId in i['@id']:
            return i['#text']
    return None

def getCatFromList(catName):
    if catName in list(const.list.keys()):
        res = const.list[catName]
        if res == '':
            return None
        return res
    else:
        return None

# def editMarkt(vkid,catVkId):
#     return ''

def addToAlbum(item_id, album_id):
    vk.market.addToAlbum(
        owner_id='-'+config.groupId,
        item_id=item_id,
        album_ids = album_id
    )
fileError = open('txt\\fileError.log','a');
vkitemAlbum = open('db\\vkitemAlbum.db','a')
for i in offer:
    if i['@id'] in site_vk_d:
        vkid = site_vk_d[i['@id']]
        if  vkid not in vkitemAlbum_list:
            print(vkid)
            catid = i['categoryId']
            сatNameS = getCatName(catid)
            #print('сatNameS',сatNameS)
            сatName = getCatFromList(сatNameS)
            if not сatName is None:
                catVkId = vk_category_d[сatName]
                addToAlbum(vkid,catVkId)
                vkitemAlbum.write(str(vkid) + ' ' + str(catid) + ' ' + str(catVkId) +'\n')
            else:
                fileError.write(str(i['@id']) + ' не найдена категория в справочнике ' + str(catid) +' '+str(сatNameS) + '\n')
    else:
        fileError.write(str(i['@id']) + ' не найдено в вк\n')