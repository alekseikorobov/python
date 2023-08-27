#получение последнего id из хабра
#для этого получаем rss, парсим и вытаскиваем первую запись id

import requests

def get_last_id_from_habr() -> int:
    xml = requests.get('https://habr.com/ru/rss/articles/all/').text

    start_str = '<guid isPermaLink="true">https://habr.com/ru/articles/'
    end_str = '/</guid>'

    left_index = xml.find(start_str)
    right_index = xml.find(end_str)

    return int(xml[left_index:right_index].replace(start_str,''))
        
if __name__ == '__main__':
    max_id = get_last_id_from_habr()
    with open('max_id_habr.txt','w') as f:
        f.write(str(max_id))