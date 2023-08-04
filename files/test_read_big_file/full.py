
# заполнение файл каким-то текстом

import os

if os.path.exists('file_res.txt'):
    os.remove('file_res.txt')
    
with open('file.txt','r') as source:
    res = source.read()    
    with open('file_res.txt','a') as dist:
        dist.write(res)

for i in range(100):
    with open('file_res.txt','r') as source:
        res = source.read()
    s = 0 #os.path.getsize('file_res.txt')
    print(f'{i=} {s=}')
    with open('file_res.txt','a') as dist:
        dist.write(res)
        