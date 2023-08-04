import requests
import os
from bs4 import BeautifulSoup

url = "https://www.cian.ru/magazine-vtorichnaya/?ordering=-date_publish&page="
data_result = []

for i in range(1,29):
    p='cache/page'+str(i)+'.html'
    if not os.path.exists(p):
        print('download -  '+ p)
        r = requests.get(url+str(i),verify=False)
        with open(p,'w', encoding='UTF-8') as f:
            f.write(r.content)
            text = r.content
    else:
        with open(p,'r', encoding='UTF-8') as f:
            text = f.read()
    soup = BeautifulSoup(text,'lxml')
    res = soup.findAll('a',{'class','list-item__title___1S-pp'})
    for r in res:
        data_result.append(r.string + '\n')

with open('result.txt','w', encoding='UTF-8') as f:
    f.writelines(data_result)