# функции для получения json статей по указанным id
# процесс не автоматизированный, функции выполняются с указанием списка id


import requests 
import os
from my_timer import measure_performance
from multiprocessing.dummy import Pool as ThreadPool
from not_found_list import not_found_list
from get_list_json import get_article

@measure_performance
def get_articles_async_by_list(list):
    pool = ThreadPool(3)
    pool.map(get_article, list)

if __name__ == '__main__':
    get_articles_async_by_list(not_found_list)