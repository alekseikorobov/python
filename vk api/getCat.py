import xmltodict,sys,const
import mass

with open('db\\index.xml') as fd:
    doc = xmltodict.parse(fd.read())

category = doc['yml_catalog']['shop']['categories']['category']

def getCatName(catId):
    for i in category:
        if catId in i['@id']:
            return i['#text']
    return None

for i in mass.i:
    print(i,getCatName(str(i)))