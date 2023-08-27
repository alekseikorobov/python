#получение последнего id из файлов
#для этого сначала берем последнюю папку
# потом берем последний id

import os

BASE_DIR = 'data'

def get_last_id_from_files() -> int:
    
    dires = os.listdir(BASE_DIR)    
    max_num = max([int(i.replace('data_','')) for i in dires])
    
    path = os.path.join(BASE_DIR,f'data_{max_num}')
    
    files = os.listdir(path)
    max_id = max([int(i.replace('articles_','').replace('.json','')) for i in files])
    return max_id
   
        
if __name__ == '__main__':
    max_id = get_last_id_from_files()
    print(f'{max_id=}')
    
    with open('max_id_file.txt','w') as f:
        f.write(str(max_id))