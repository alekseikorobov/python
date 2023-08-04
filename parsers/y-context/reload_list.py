from requests_html import HTMLSession
import requests
session = HTMLSession()

cookies_str = 'yandexuid=id;'

from http.cookiejar import Cookie, CookieJar    # Python 3

def make_cookiejar_dict(cookies_str):
    # alt: `return dict(cookie.strip().split("=", maxsplit=1) for cookie in cookies_str.split(";"))`
    cookiejar_dict = {}
    for cookie_string in cookies_str.split(";"):
        # maxsplit=1 because cookie value may have "="
        cookie_key, cookie_value = cookie_string.strip().split("=", maxsplit=1)
        cookiejar_dict[cookie_key] = cookie_value
    return cookiejar_dict

dt = make_cookiejar_dict(cookies_str)
cj = requests.utils.cookiejar_from_dict(make_cookiejar_dict(cookies_str))

def d_link(url):
    with open('links.txt','a') as f:        

        r = session.get(url, cookies=cj)

        contest_head = r.html.find('.contest-head__item.contest-head__item_role_title', first=True)
        if contest_head:
            a = contest_head.find('a', first=True)

            btn_registr = r.html.find('.button_local-theme_register', first=True)
            is_reg = 'true' if btn_registr else 'false'
            #print('btn_registr',btn_registr,is_reg)

            f.write(f'{url}|{a.text}|{is_reg}\r\n')
            print(f'{url}')
        else:
            print(f'{url} not exists')


#d_link('https://contest.yandex.ru/contest/20030/enter/')

with open('links_4_20000.md','r') as f:
    h1 = f.readline()
    h2 = f.readline()
    line = "start"    
    while line:
        line = f.readline()
        if len(line)>1:
            d_link(line.split()[0].strip())            
