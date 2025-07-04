#%%
import requests
from pprint import pprint
#%%



url = "https://api.hh.ru/vacancies?text=Data science"


res = requests.get(url)
data = res.json()
#%%
data.keys()
#%%
for key in data.keys():
    print(key,type(data[key]))

#%%
print('items',len(data['items']))
print('found',data['found'])
print('pages',data['pages'])
print('page',data['page'])
print('per_page',data['per_page'])
print('clusters',data['clusters'])
print('arguments',data['arguments'])
print('fixes',data['fixes'])
print('suggests',data['suggests'])
print('alternate_url',data['alternate_url'])
#%%
pprint(data['items'][0])
#%%
for item in data['items']:
    print(item['department'], item['name'])