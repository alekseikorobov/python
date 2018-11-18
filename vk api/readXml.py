# -*- coding: utf-8 -*-
import xmltodict
import sys
import const

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

def getCatName(catId):
    for i in category:
        if catId in i['@id']:
            return const.list[i['#text']]


def editMarkt(vkid,catVkId):
    return ''

for i in offer:
    if i['@id'] in site_vk_d:
        vkid = site_vk_d[i['@id']]
        catid = i['categoryId']
        сatName = getCatName(catid)
        catVkId = vk_category_d[сatName]
        editMarkt(vkid,catVkId)
        print(vkid,catid,catVkId)