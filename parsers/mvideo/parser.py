#%%
import pandas as pd
from bs4 import BeautifulSoup
import re

with open(f'data/example.html') as f:
    soup = BeautifulSoup(f.read())
#%%
elements = soup.find_all(class_ = 'product-card-wrapper')
len(elements)
#%%
def get_params(element):
    result = {
        'price':0,
        'link':None,
        'title':None,
        'rating':None,
        'feedback_count':None
    }
    price_element = element.find(class_='price__main-value')    
    result['price'] = int(price_element.get_text().strip().replace('\xa0','').replace('₽',''))    
    product_title_element = element.find(class_='product-title__text')
    result['link'] = 'https://www.mvideo.ru'+product_title_element.attrs['href']
    product_title = product_title_element.get_text().strip()
    result['title'] = product_title
    product_rating_element = element.find(class_='product-rating')
    value_element = product_rating_element.find(class_ = 'value')
    if value_element is not None:
        rating_value = float(value_element.get_text())
        result['rating'] = rating_value
    product_rating_element = element.find(class_='product-rating')
    product_rating__feedback_element = product_rating_element.find(class_ = 'product-rating__feedback')
    if product_rating__feedback_element is not None:
        feedback_str = product_rating__feedback_element.get_text().strip()        
        if feedback_str != 'нет отзывов':                
            try:
                feedback_value = re.match(r'\d+',feedback_str)
                feedback_value = int(feedback_value.group(0))
                result['feedback_count'] = feedback_value
            except Exception as ex:
                print('feedback_str',feedback_str)
                raise(Exception(ex))
    return result

def get_all_elements(soup):
    results = []
    elements = soup.find_all(class_ = 'product-card-wrapper')
    print(len(elements))
    for element in elements:
        result = get_params(element)
        
        results.append(result)
    return results

results = get_all_elements(soup)
print(len(results))
# %%
pd.DataFrame(results).to_excel('data/result_20250206.xlsx')