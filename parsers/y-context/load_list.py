from requests_html import HTMLSession
session = HTMLSession()


def d_link(id):
    with open('links.txt','a') as f:
        url = f'https://contest.yandex.ru/contest/{id}/enter/'
        r = session.get(url)
        contest_head = r.html.find('.contest-head__item.contest-head__item_role_title', first=True)
        if contest_head:
            a = contest_head.find('a', first=True)
            f.write(f'{url}\t{a.text}\r\n')
            print(f'{id} - {a.text}')
        else:
            print(f'{id} not exists')
start = 10000
for id in range(start*2,start*4):
    d_link(id)
