#coding=utf-8
# -*- coding: utf-8 -*-
import xmltodict
import os,time,sys,argparse,datetime,re
import requests

with open('db\\index.xml') as fd:
    doc = xmltodict.parse(fd.read())
pathUsAlbum = 'c:\\myProject\\python\\vk api\\images\\'
def saveImage(url):
    global pathUsAlbum;
    re = requests.get(url)
    title = url.split('/')[-1]
    fulllocalname = os.path.join(pathUsAlbum, '%s' % title)
    if not os.path.isfile(fulllocalname):
            with open(fulllocalname, 'wb') as f:
                for buf in re.iter_content(1024):
                    if buf:
                        f.write(buf)

    return fulllocalname;

offer = doc['yml_catalog']['shop']['offers']['offer']
listNotImage = []

filelocal = open('db\\fileJpg.db','w+')
count = 0
countAll = len(offer);
for i in offer:
    if 'picture' in i:
        fulllocalname = saveImage(i['picture'])        
        filelocal.write(i['@id'] + '\t' + fulllocalname + '\n')
        count = count + 1
        print(count,'\t',count/countAll*100,'%')
    else:
        listNotImage.append(i['url'])
