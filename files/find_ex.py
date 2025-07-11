# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

скрипт составляет список всех расширений по заданному пути и сортирует по 
колличеству

http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
"""

import os
import operator
import requests,io
i = 0
f = io.open('data.txt','w',encoding='utf8')
path = '.'
d = {'.':0};
for top,dirs,files in os.walk(path):
    print(top)
    for nm in files:
        bn = os.path.basename(nm);
        if '.' in bn:
            ex = bn.rsplit('.', 1)[1];
            if(ex in d):
                d[ex] = d[ex] + 1;
            else:
                d[ex] = 1;
        else:
            d['.'] = d['.'] + 1;


sorted_x = sorted(d.items(), key=operator.itemgetter(1));

#for w in sorted(d, key=d.get, reverse=True):
 # print w, d[w]

for k,v in sorted_x:
    try:
        s = str(k) + ' ' + str(v);
        print(str(s));
        f.writelines(str(s) + u'\n');
    except Exception as ex:
        print ex
    
    
f.close();
