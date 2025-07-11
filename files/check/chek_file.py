



import os

path1 = os.getenv('BASE_PATH_PHOTO_1')
path2 = os.getenv('BASE_PATH_PHOTO_2')
path3 = os.getenv('BASE_PATH_PHOTO_3')

def check_file(line):
    #print(line)
        
    full_path = os.path.join(path1,line)
    if os.path.isfile(full_path):
        return 'OK',full_path
    
    full_path = os.path.join(path2,line)
    if os.path.isfile(full_path):
        return 'OK',full_path
    
    full_path = os.path.join(path3,line)
    if os.path.isfile(full_path):
        return 'OK',full_path
    
    print(f'{full_path=}')
    
    return 'not',None
i = 0
with open('files.txt','r') as f:
    for line in f.readlines():
        line = line.strip()
        s, path = check_file(line)
        if s == 'not':
            #print(line)
            i += 1
print(i)

line = '2024-09-26 15-37-20.MOV'

full_path = os.path.join(path2,line)

#full_path = '/media/aleksei/data/cloud/yandex/Загрузки/Фотокамера (1)/2024/'
print(os.path.isfile(full_path))
