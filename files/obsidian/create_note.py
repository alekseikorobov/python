# получаем из буфера ссылку
# по этой ссылке 
# 1. определяем какой сайт
# 2. парсим сайт
# 3. создаем заметку с заданным шаблоном

from pytubefix import YouTube
import requests
import clipboard
import re
import json
from urllib.parse import urlparse
from loguru import logger
from bs4 import BeautifulSoup
from string import Template
from datetime import datetime
import os
import template
import dotenv
import hashlib
from notify import notification
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

dotenv.load_dotenv()
BASE_PATH_OBSIDIAN = os.getenv("BASE_PATH_OBSIDIAN")
BASE_PATH_OBSIDIAN_LEETCODE = os.getenv("BASE_PATH_OBSIDIAN_LEETCODE")
BASE_PATH_CACHE_OBSIDIAN_HTML = os.getenv("BASE_PATH_CACHE_OBSIDIAN_HTML")
if not os.path.isdir(BASE_PATH_CACHE_OBSIDIAN_HTML):
    os.makedirs(BASE_PATH_CACHE_OBSIDIAN_HTML)

if not os.path.isfile("log/obsidian_create_note.log"):
    raise(Exception('not file path'))

SOURCE_DATE_FORMATTER = "%Y-%m-%d %H:%M:%S"

logger.add("log/obsidian_create_note.log", enqueue=True, rotation="500 MB")

def validate_url(text):
    '''
    проверить c помощью регуряного выражения что текст является ссылкой
    '''
    pattern = r'^http(s|)?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    if re.match(pattern, text):
        return True
    else:
        return False
        
def get_domain_from_url(url:str):
    '''
    получить домен из ссылки
    '''    
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain = domain.replace('www.','')
    return domain


store_links = set([])
def get_or_create_from_store_youtube(url:str):
    path_links = os.path.join(BASE_PATH_CACHE_OBSIDIAN_HTML,'links.txt')
    if os.path.isfile(path_links):
        with open(path_links,'r') as f:
            for line in f.readlines():
                line = line.strip()
                store_links.add(line)
    url_md5 = hashlib.md5(url.encode()).hexdigest()
    path_url_json = os.path.join(BASE_PATH_CACHE_OBSIDIAN_HTML, url_md5+'.json')
    obj = {}
    if url in store_links:
        #кодируем url в md5
        if os.path.isfile(path_url_json):
            with open(path_url_json,'r') as f:
                obj = json.load(f)
                logger.info(f'взяли файл {url_md5} из кеша по урлу {url}')
        else:
            raise(Exception(f'какая-то ошибка НЕТ html файла по url = {url}'))
    else:
        obj = get_meta_from_youtube(url)
        with open(path_url_json,'w') as f:
            json.dump(obj,f)
        with open(path_links,'a') as f:
            f.write(url + '\n')            
    return obj

import requests
from bs4 import BeautifulSoup

def get_leetcode_content(url:str):
    # Создаем сессию для сохранения cookies между запросами
    session = requests.Session()
    
    # Устанавливаем заголовки, чтобы имитировать браузер
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        # Первый запрос для получения cookies
        print("Делаем первый запрос для получения cookies...")
        response1 = session.get(url, headers=headers, timeout=10)
        print(f"Первый запрос: статус {response1.status_code}")
        
        # Второй запрос с полученными cookies
        print("Делаем второй запрос с cookies...")
        response2 = session.get(url, headers=headers, timeout=10)
        print(f"Второй запрос: статус {response2.status_code}")
        
        # Проверяем успешность запроса
        if response2.status_code == 200:
            # Используем BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(response2.text, 'html.parser')
            
            # Извлекаем заголовок страницы
            title = soup.find('title')
            if title:
                print(f"Заголовок страницы: {title.text}")
            
            # Можно извлечь другую информацию
            # Например, найти все ссылки
            links = soup.find_all('a', href=True)
            print(f"Найдено ссылок: {len(links)}")
            
            return response2.text
        else:
            print(f"Ошибка: статус код {response2.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

# Альтернативный вариант с более сложными настройками
def get_leetcode_with_detailed_headers(url:str):
    session = requests.Session()
    
    # Более детальные заголовки
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
    }
    
    try:
        # Первый запрос для инициализации сессии
        response = session.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print("Успешно получена страница!")
            print(f"Размер ответа: {len(response.text)} символов")
            print(f"Получено cookies: {len(session.cookies)}")
            
            # Выводим некоторые cookies
            for cookie in session.cookies:
                print(f"Cookie: {cookie.name} = {cookie.value}")
                
            return response.text
        else:
            print(f"Ошибка: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def get_or_create_from_store(url:str,chage=False,not_use_store = False):    
    path_links = os.path.join(BASE_PATH_CACHE_OBSIDIAN_HTML,'links.txt')
    if not not_use_store and os.path.isfile(path_links):
        with open(path_links,'r') as f:
            for line in f.readlines():
                line = line.strip()
                store_links.add(line)
    url_md5 = hashlib.md5(url.encode()).hexdigest()
    path_url_html = os.path.join(BASE_PATH_CACHE_OBSIDIAN_HTML, url_md5+'.html')
    html = ''
    if url in store_links:
        #кодируем url в md5
        if os.path.isfile(path_url_html):
            with open(path_url_html,'r') as f:
                html = f.read()
                logger.info(f'взяли файл {url_md5} из кеша по урлу {url}')
        else:
            raise(Exception(f'какая-то ошибка НЕТ html файла по url = {url}'))
    else:
        if chage:
            
            #html = get_leetcode_content(url)
            html = get_leetcode_with_selenium(url)
            # with requests.session
            # headers = {
            #     'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #     #'accept-encoding':'gzip, deflate, br, zstd',
            #     'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            #     'dnt':'1',
            #     'pragma':'no-cache',
            #     'priority':'u=0, i',
            #     'sec-ch-ua':'"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            #     'sec-ch-ua-mobile':'?0',
            #     'sec-ch-ua-platform':'"Linux"',
            #     'sec-fetch-dest':'document',
            #     'sec-fetch-mode':'navigate',
            #     'sec-fetch-site':'same-origin',
            #     'sec-fetch-user':'?1',
            #     'upgrade-insecure-requests':'1',
            #     'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'                
            # }
            # response = requests.get(url,headers=headers)
            # html = response.text
        else:
            response = requests.get(url)
            html = response.text
        logger.info(f'save to {path_url_html=}')
        with open(path_url_html,'w') as f:
            f.write(html)
        with open(path_links,'a') as f:
            f.write(url + '\n')            
    return html

def tag_fix(tag:str):
    return tag.strip().replace(' ','_')

def parse_size_html(url:str):
    html = get_or_create_from_store(url)
    result = {
        'title':'',
        'duration':'',
        'tags':[],
    }
    soup = BeautifulSoup(html, 'html.parser')
    if soup.title is not None:
        result['title'] = soup.title.get_text()
    return result

def parse_habr_html(url:str):
    # return {'title': 'Нормализация vs Денормализация: Mongo, Postgres и реальная жизнь', 
    #         'reading-time': '17 мин', 
    #         'tags': ['PostgreSQL *', 'MongoDB *', 
    #                  'Базы данных *', 'Анализ и проектирование систем *', 'Микросервисы *']
    #         }
    #return {'title': 'Как устроен алгоритм CRF и какие возможности он имеет'}
    
    html = get_or_create_from_store(url)
    
    result = {
        'title':'',
        'duration':'',
        'source_date':'',
        'tags':[],
    }
    soup = BeautifulSoup(html, 'html.parser')
    #logger.info(soup.title)
    
    title_element = soup.find(attrs={"class": "tm-title tm-title_h1"})
    
    if title_element is not None:
        result['title'] = title_element.get_text()
    
    datetime_published_element = soup.find(attrs={'class':'tm-article-datetime-published'})
    if datetime_published_element is not None:
        time_element = datetime_published_element.find('time')
        if time_element is not None:
            datetime_value = time_element.attrs['datetime'] #example 2025-01-12T14:15:10.000Z
            datetime_value = datetime.strptime(datetime_value, '%Y-%m-%dT%H:%M:%S.%fZ').strftime(SOURCE_DATE_FORMATTER)
            result['source_date'] = datetime_value
    
    reading_time_element = soup.find(attrs={"class": "tm-article-reading-time__label"})    
    if reading_time_element is not None:
        result['duration'] = reading_time_element.get_text()
        
    hab_elements = soup.find_all(attrs={"class": "tm-publication-hub__link-container"})
    if hab_elements is not None and len(hab_elements)>0:
        tags = []
        for element in hab_elements:
            if element is None: continue
            a_element = element.find('a')
            if a_element is None: continue
            span_element = a_element.find('span')
            if span_element is None: continue
            t = span_element.get_text()
            if t is not None and t != '':                
                tag_name = tag_fix(t)
                tags.append(tag_name)
        result['tags'] = tags
        
    return result

def create_file_name(title:str,template='learn'):
    
    #замена спецсимволов
    title = re.sub(r'[^\w\s-]', '', title).strip()
    title = re.sub(r' +', ' ', title)
    #title = title.replace(' ', '_')
    if template == 'learn':
        if BASE_PATH_OBSIDIAN is None:
            raise Exception(f'not correct param BASE_PATH_OBSIDIAN')
        
        return os.path.join(BASE_PATH_OBSIDIAN, title + '.md')
    if template == 'leetcode':
        if BASE_PATH_OBSIDIAN_LEETCODE is None:
            raise Exception(f'not correct param BASE_PATH_OBSIDIAN_LEETCODE')
        title = title.lower()
        return os.path.join(BASE_PATH_OBSIDIAN_LEETCODE, title + '.md')
    
def get_week_from_date(now:datetime):
    '''
    получение номера недели
    '''    
    week_number = now.isocalendar()[1]
    
    return week_number
    
def object_to_obsidian(obj,template = 'learn'):
    if obj['title'] == '':
        t = f'not correct parsing html'
        logger.warning(t)
        return 'warn', t
    #logger.info(obj)
    
    full_path_to_file = create_file_name(obj['title'],template=template)
    if os.path.isfile(full_path_to_file):
        _,name = os.path.split(full_path_to_file)
        t = f'file exist {name}'
        logger.warning(t)
        return 'warn', t
    if template == 'learn':
        return object_to_obsidian_learn(obj, full_path_to_file)
    if template == 'leetcode':        
        return object_to_obsidian_leetcode(obj, full_path_to_file)
    
    return None,None

def object_to_obsidian_leetcode(obj, full_path_to_file):
    
    #получение текущей даты в формате YYYY-MM-DD HH:mm:ss
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
    
    #получение номера текущей недели от начала года
    week = get_week_from_date(now)
    
    topics = ''
    if 'topics' in obj and obj['topics'] is not None and len(obj['topics'])>0:
        topics = '\n  '
        topics += '\n  '.join([f'- "{t}"' for t in obj['topics']])
        
    tags = ''
    if 'tags' in obj and obj['tags'] is not None and len(obj['tags'])>0:
        tags = '\n  '
        tags += '\n  '.join([f'- "{t}"' for t in obj['tags']])
    
    description = ''
    if 'description' in obj and obj['description'] is not None and len(obj['description'])>0:
        description = obj['description']
        
        description = description.replace('$','$$')
    
    dif = {
        'Easy':'⭐',
        'Medium':'⭐⭐',
        'Hard':'⭐⭐⭐',
        '':'',
    }[obj['difficulty']]
    
    # logger.info('description:')
    # logger.info(description)
    #заполенние параметров
    params = {
        'difficulty': dif,
        'add_dt': dt,        
        'topics': topics,
        'link': obj['url'],
        'tags': tags,
        'description': description,
        'sim_questions': ''
    }
    logger.info(params)
    text = Template(template.TEMPLATE_LEETCODE).substitute(params)
    
    with open(full_path_to_file,'w') as f:
        f.write(text)
    
    msg = f'created file {full_path_to_file=}'
    logger.info(msg)
    
    return 'done', msg

def object_to_obsidian_learn(obj, full_path_to_file):
    
    #получение текущей даты в формате YYYY-MM-DD HH:mm:ss
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
    
    #получение номера текущей недели от начала года
    week = get_week_from_date(now)
    
    tags = ''
    if 'tags' in obj and obj['tags'] is not None and len(obj['tags'])>0:
        tags = '\n  '
        tags += '\n  '.join([f'- "#{t}"' for t in obj['tags']])
    
    description = ''
    if 'description' in obj and obj['description'] is not None and len(obj['description'])>0:
        description = obj['description']
    
    source_date = ''
    if 'source_date' in obj and obj['source_date'] is not None:
        source_date = obj['source_date']
    
    #заполенние параметров
    params = {
        'type': obj['type'],
        'add_dt': dt,
        'week': week,
        'source': obj['source'],
        'link': f"{obj['url']}",
        'duration': obj['duration'],
        'tags': tags,
        'description': description,
        'source_date': source_date,
    }
    text = Template(template.TEMPLATE_NOTE).substitute(params)
    
    with open(full_path_to_file,'w') as f:
        f.write(text)
    
    msg = f'created file {full_path_to_file=}'
    logger.info(msg)
    
    return 'done', msg

def habr_handler(url:str,tags=[]):
    '''
    обработка ссылки habr
    '''
    logger.info(f'habr {url}')
    obj = parse_habr_html(url)
    obj['url'] = url
    obj['type'] = '"[[Статья]]"'
    obj['source'] = 'habr'
    return object_to_obsidian(obj)

def site_handler(url:str,domain:str,tags=[]):
    '''
    обработка общих ссылок 
    '''
    logger.info(f'site {url}')
    obj = parse_size_html(url)
    obj['url'] = url
    obj['type'] = '"[[Статья]]"'
    obj['source'] = domain
    return object_to_obsidian(obj)

def get_meta_from_youtube(url:str):
    # return {'title': 
    #     'Avito Tech | ML System design game. Practice', 'duration': '6875', 'views': '', 
    #     'description': 'Онлайн практика в ODS спейсе Spatial.Chat\nАктивность от организаторов секции ML in Marketplace\n\n\nСтраница мероприятия Data Fest 2024: https://ods.ai/events/datafest2024\nВсе доклады и презентации секции ML in Marketplace вы можете найти в треке: https://ods.ai/tracks/df24-mlavitotech\nОфлайн встреча Data Fest 2024 в гостах у Авито 1 июня 2024 года: https://ods.ai/events/fest2024-avito-msc\nСтраница мероприятия Data Fest 2024: https://ods.ai/events/datafest2024\n\n\n----\nНаши соц.сети:\n\nODS Events (мероприятия сообщества) https://t.me/datafest\nODS Jobs (вакансии сообщества) https://t.me/odsjobs\nODS Courses (апдейты по бесплатным курсам от сообщества) https://t.me/odscourses\n\nODS YouTube https://www.youtube.com/@ODSAIRu\nВконтакте группа https://vk.com/datafest\nЧат в Mattermost https://ods.ai/tracks/mattermost', 
    #     'publish_date': '2024-10-06 04:53:38-07:00'
    #         }
    logger.info(f'start parsing - {url}')
    yt = YouTube(url)
    
    result = {
        'title': '',
        'duration': '',
        'description': '',
        'source_date': ''
    }
    result['title'] = yt.title
    #logger.info(vars(yt))
    #duration = str(ty.duration // 3600) + ":" + str((ty.duration // 60) % 60).zfill(2) + ":" + str(ty.duration % 60).zfill(2)
    try:
        result['duration'] = str(yt.length)
    except Exception as ex:
        logger.error(f'duration - {ex}')

    #result['views'] = str(yt.views) #не работает!
    try:
        if yt.publish_date is not None:
            result['source_date'] = yt.publish_date.strftime(SOURCE_DATE_FORMATTER)
    except Exception as ex:
        logger.error(f'publish_date - {ex}')
        
    try:
        result['description'] = yt.description
    except Exception as ex:
        logger.error(f'publish_date - {ex}')
    
    #logger.info(result)
    return result
        
def youtube_handler(url:str,tags=[]):
    '''получение основной информации с youtube по url'''   
    
    try:
        obj = get_or_create_from_store_youtube(url)
        obj['url'] = url
        obj['type'] = '"[[video]]"'
        obj['source'] = 'youtube'
        return object_to_obsidian(obj)

    except Exception as e:
        t = f'error parsing youtube video: {e}'
        logger.warning(t)
        return 'warn', t
    
def get_text_by_class(soup, class_name:str):
    value = ''
    title_element = soup.find(attrs={"class": class_name})
    if title_element is not None:
        value = title_element.get_text()
    return value

def get_list_text_by_class(soup, class_name:str)->list:
    topic_elements = soup.find_all(attrs={'class':class_name})
    result = []
    if topic_elements is not None and len(topic_elements)>0:
        for topic_element in topic_elements:
            val = topic_element.get_text()
            if val is not None and len(val)>0:
                result.append(val)    
    return result

def parse_leetcode_html(html:str):    
    result = {
        'title':'',
        'difficulty':'',
        'topics':[],
        'add_dt':'',
        'url':'',
        'tags':[],
        'description':'',
        'sim_questions':'',
    }
    soup = BeautifulSoup(html, 'html.parser')
    #logger.info(soup.title)
    
    result['title'] = get_text_by_class(soup, "text-title-large")
    
    result['difficulty'] = get_text_by_class(soup, "text-difficulty-easy")
    if result['difficulty'] == '':
        result['difficulty'] = get_text_by_class(soup, "text-difficulty-medium")
    elif result['difficulty'] == '':
        result['difficulty'] = get_text_by_class(soup, "text-difficulty-hard")
    
    result['description'] = get_text_by_class(soup, "elfjS")
        
    cl = 'no-underline hover:text-current relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-text-secondary'
    result['topics'] = get_list_text_by_class(soup,cl)    
    result['topics'] = [x.replace(' ', '_') for x in result['topics']]
            
    logger.info(result)
    return result
    
def get_leetcode_with_selenium(url):
    # Настройки Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Работа в фоне
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(3)  # Ждем загрузки JavaScript
        
        # Получаем содержимое страницы
        page_source = driver.page_source
        print(f"Размер страницы: {len(page_source)} символов")
        
        # Можно извлекать конкретные элементы
        title = driver.title
        print(f"Заголовок: {title}")
        
        return page_source
        
    finally:
        driver.quit()
    
def leetcode_handler(url:str,tags=[]):
    '''получение из leetcode заголовка и меты'''
    html = get_or_create_from_store(url,chage=True)#,not_use_store=True)
    
    obj = parse_leetcode_html(html)
    obj['url'] = url
    obj['tags'] = tags
    return object_to_obsidian(obj,template = 'leetcode')

def handler(text,notify=True,tags=[]):
    v = validate_url(text)
    if not v:
        t = f'text not link {len(text)} {text}'
        logger.warning(t)
        return 'warn', t
    if notify:
        notification('obsidian', message=f'получена ссылка {text} взяли в работу', app_name='obsidian',timeout = 10000)
    
    domain = get_domain_from_url(text)
    if domain == 'habr.com':
        status, result = habr_handler(text,tags=tags)
        return status, result
    elif domain == 'youtube.com':
        status, result = youtube_handler(text,tags=tags)
        return status, result
    elif domain == 'leetcode.com':
        status, result = leetcode_handler(text,tags=tags)
        return status, result
    else:
        status, result = site_handler(text,domain,tags=tags)
        return status, result
    
    return '',''


def from_buffer():
    
    status, result = '',''
    
    try:
        text = clipboard.paste()
        #text = 'https://www.youtube.com/watch?v=1Bf0_QXyyIY'
        #text = 'https://leetcode.com/problems/longest-palindromic-substring/description/'        
        #text = 'https://leetcode.com/problems/longest-palindromic-substring/description/'
        #text = 'https://leetcode.com/problems/two-sum/description/'
        #text = 'http://www.machinelearning.ru/wiki/index.php?title=%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%BA%D1%83%D1%80%D1%81_%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B9,_%D0%9A.%D0%92.%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D1%86%D0%BE%D0%B2)'
        status, result = handler(text)
    except Exception as ex:
        result = f'{ex}'
        logger.exception(ex)
        
        status = 'error'
        
    signe = {
        'error':'❌',
        'warn':'⚠️',
        'done':'✅',
        '':'',
    }
    signe = signe[status]
    
    notification('obsidian', message=f'{signe} {result.upper()}', app_name='obsidian',timeout = 10000)

    
    #url = 'https://habr.com/ru/articles/837324/'
    #habr_handler(url)

if __name__ == '__main__':    
    #mass_upload()
    from_buffer()
    
