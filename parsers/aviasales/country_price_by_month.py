# скрипт получает данные из aviasales по всем странам и всем городам средние цены за каждый месяц

import requests, os, json, csv

if not os.path.isdir('data'):
    os.mkdir('data')

def get_months(destination_code,origin_code = "MOW"):
    r = requests.post('https://content-admin.aviasales.ru/api/widgets', json=
        {"operation_name": "fetch_seasonal",
        "app":"selene",
        "query":"""{
    widgets {
        directionsMonthsV1(origin: \""""+origin_code+"""\", destination: \""""+destination_code+"""\", locale: \"ru_RU\", oneWay: true, currency: \"rub\") {
        
        months {
            departMonth
            season
            price
            temperature
            precipitation
        }
        }
    }
    }"""
        }
    )
    #return r.json()
    #print(r.text)
    return r.text


#print(get_months("CAI"))
def get_country_list():
    country_json = {}
    if not os.path.isfile('supported_directions.json'):
        country_url = "https://map.aviasales.ru/supported_directions.json?origin_iata=MOW&locale=ru"
        r = requests.get(country_url)
        with open('supported_directions.json','w',encoding='UTF-8') as f:
            f.write(r.text)
        country_json = r.json()


    with open('supported_directions.json','r',encoding='UTF-8') as f:
        text = f.read()
        country_json = json.loads(text)
    return country_json


if not os.path.isfile('country.txt'):
    country_json = get_country_list()
    with open('country.txt','w',encoding='UTF-8') as f:
        line = 'direct' + '\t' + 'iata' + '\t' + 'name' + '\t' + 'country' + '\t' + 'country_name' + '\n'
        f.write(line)
        for index in range(0, len(country_json['directions'])):
            d = country_json['directions'][index]
            line = str(d['direct']) + '\t' + str(d['iata']) + '\t' + str(d['name']) + '\t' + str(d['country']) + '\t' + str(d['country_name']) + '\n'
            f.write(line)


country_json = get_country_list()

headers = ['iata','name','country','country_name','departMonth','precipitation','price','season','temperature']
if not os.path.isfile('country_price_by_month.csv'):
    with open('country_price_by_month.csv', 'w',encoding='1251', newline='', errors='ignore') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(headers)
        for index in range(0, len(country_json['directions'])):
            d = country_json['directions'][index]
            iata = str(d['iata'])
            print('get by ' + iata)
            path = 'data/code_'+iata + '.json'
            if not os.path.isfile(path):
                print('load...' )
                text = get_months(iata)
                print('save to file')
                with open(path,'w',encoding='UTF-8') as f1:
                    f1.write(text)
            
            months_json = {}
            with open(path,'r',encoding='UTF-8') as f1:
                t = f1.read()
                months_json = json.loads(t)
            for m in months_json['data']['widgets']['directionsMonthsV1']['months']:
                line = [str(d['iata']),str(d['name']),str(d['country']),str(d['country_name']),str(m['departMonth']),str(m['precipitation']),str(m['price']),str(m['season']),str(m['temperature'])]
                #print(line)
                spamwriter.writerow(line)