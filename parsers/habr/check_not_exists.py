#проверка каких файлов не существует
#перебираем все id, до максимального, и если не найдено выводим на экрано


import os
from my_timer import measure_performance

@measure_performance
def get_all_id_from_file_name():
    ids = set()
    for root,dirs,files in os.walk('data/data_1'):
        for file in files:
            if 'articles_' in file and '.json' in file:
                id = int(file.replace('articles_','').replace('.json',''))
                ids.add(id)
    return ids

@measure_performance
def get_not_eixts(ids):
    max_id = max(ids)
    min_id = min(ids)
    print(f'{min_id=}, {max_id=}')     #min_id=1, max_id=983481
    ids_all=set()
    for index in range(min_id,max_id):
        ids_all.add(index)
        
    return list(ids_all - ids)

ids = get_all_id_from_file_name()
print(f'{len(ids)=}')
not_exists_ids = get_not_eixts(ids)
print(f'{len(not_exists_ids)=}')
print(f'{not_exists_ids=}')

