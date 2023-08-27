#получение статей по указанным ID
#настроена следующая автоматизация:
# 1. получение максимального id из сервера habr.com
# 2. получение максимального id из файлов
# 3. по указанному диапазону скачиваеются статьи в виде json файлов
    # 3.1. статиь размещаются в папку с номером id // 20_000, если папки нет, создается


import requests 
import os
from my_timer import measure_performance
from multiprocessing.dummy import Pool as ThreadPool
from get_last_index_from_files import get_last_id_from_files
from get_last_index_from_habr import get_last_id_from_habr

BASE_DIR = 'data'

def get_article(index):
    #print(f'{index=}')
    req = requests.get(f'https://habr.com/kek/v2/articles/{index}')
    nom = index // 20_000
    directory = os.path.join(BASE_DIR, f'data_{nom}')
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(os.path.join(directory,f'articles_{index}.json'),'w') as f:
        f.write(req.text)

@measure_performance
def update_article_list():
    start_id = get_last_id_from_files() + 1
    end_id = get_last_id_from_habr()

    if start_id > end_id:
        print(f'все статиь уже получены')
    else:
        pool = ThreadPool(3)
        pool.map(get_article, range(start_id, end_id))

if __name__ == '__main__':
    update_article_list()