#перевод статей из json файлов в таблицу pandas DataFrame

import os,json
import pandas as pd
from my_timer import measure_performance
BASE_DIR = 'data'

keys = ['id',
'timePublished',
'isCorporative',
'lang',
'titleHtml',
'postType',
'postLabels',
'author_id',
'author_alias',
'author_fullname',
'statistics_commentsCount',
'statistics_favoritesCount',
'statistics_readingCount',
'statistics_score',
'statistics_votesCount',
'statistics_votesCountPlus',
'statistics_votesCountMinus',
'hubs',
'flows',
'relatedData',
'textHtml_len',
'tags',
'metadata_dateModified',
'metadata_datePublished',
'polls',
'commentsEnabled_status',
'commentsEnabled_reason',
'rulesRemindEnabled',
'votesEnabled',
'status',
'plannedPublishTime',
'checked',
'hasPinnedComments',
'format',
'banner',
'multiwidget',
'readingTime',
'complexity',
'isEditorial']
df = pd.DataFrame(columns=keys)

def get_date_from_schemaJsonLd(json_str):
    obj = json.loads(json_str)
    return obj['dateModified'],obj['datePublished']

def get_row(path):
    row = {}
    with open(path,'r') as f:
        res = json.load(f)
        if 'id' in res:
            dateModified,datePublished = get_date_from_schemaJsonLd(res['metadata']['schemaJsonLd'])            
            row = {
                'id':int(res['id']),
                'timePublished':res['timePublished'],
                'isCorporative':res['isCorporative'],
                'lang':res['lang'],
                'titleHtml':res['titleHtml'],
                'postType':res['postType'],
                'postLabels': '',#res['postLabels'], список пустой
                'author_id':res['author']['id'] if res['author'] is not None else None,
                'author_alias':res['author']['alias'] if res['author'] is not None else None,
                'author_fullname':res['author']['fullname'] if res['author'] is not None else None,
                'statistics_commentsCount':res['statistics']['commentsCount'],
                'statistics_favoritesCount':res['statistics']['favoritesCount'],
                'statistics_readingCount':res['statistics']['readingCount'],
                'statistics_score':res['statistics']['score'],
                'statistics_votesCount':res['statistics']['votesCount'],
                'statistics_votesCountPlus':res['statistics']['votesCountPlus'],
                'statistics_votesCountMinus':res['statistics']['votesCountMinus'],
                'hubs':';'.join(i['titleHtml'] for i in res['hubs']),
                'flows':';'.join(i['titleHtml'] for i in res['flows']),
                'relatedData':'',#res['relatedData'], #value none!!!!
                'textHtml_len':len(res['textHtml']),
                #'textHtml_count_words':get_count_words_from_str(res['textHtml']),
                'tags':';'.join(i['titleHtml'] for i in res['tags']),
                'metadata_dateModified':dateModified,
                'metadata_datePublished':datePublished,
                'polls':'',#res['polls'], список пустой
                'commentsEnabled_status':res['commentsEnabled']['status'],
                'commentsEnabled_reason':res['commentsEnabled']['reason']
                ,'rulesRemindEnabled':res['rulesRemindEnabled']
                ,'votesEnabled':res['votesEnabled']
                ,'status': res['status']
                ,'plannedPublishTime':None#res['plannedPublishTime'] #value none!!!!
                ,'checked':None #res['checked'] #value none!!!!
                ,'hasPinnedComments':res['hasPinnedComments']
                ,'format':None #res['format'] #value none!!!!
                ,'banner':None #res['banner'] #value none!!!!
                ,'multiwidget':None #res['multiwidget'] #value none!!!!
                ,'readingTime':res['readingTime']
                ,'complexity':None #res['complexity'] #value none!!!!
                ,'isEditorial':res['isEditorial']
            }            
        elif 'httpCode' in res:
            file_name = os.path.basename(path)
            file_name = os.path.splitext(file_name)[0]
            id = int(file_name.replace('articles_',''))            
            row = {
                'id':id
            }
        else:
            print(res)
    return row
    
def rows_to_df(rows):
    global df    
    df1 = pd.DataFrame(rows)
    df = pd.concat([df, df1])
            
        

# path = '/home/aleksei/MyProject/python/parsers/habr/data/data_3/articles_60011.json'
# file_to_df(path)
# path = '/home/aleksei/MyProject/python/parsers/habr/data/data_3/articles_60007.json'
# file_to_df(path)

#print(df.info())
@measure_performance
def files_to_df():
    max_pull = 10000
    all_added = 0
    rows = []
    all_files = 0
    for root,dirs,files in os.walk('/home/aleksei/MyProject/python/parsers/habr/data'):
        for file in files:
            all_files+= 1
            path = os.path.join(root,file)
            row = get_row(path)
            rows.append(row)
            if all_files % max_pull == 0:
                rows_to_df(rows)
                all_added += len(rows)
                print(f'add {len(rows)=} {all_added=}')
                rows = []
        if len(rows) > 0:
            rows_to_df(rows)
            all_added += len(rows)
            print(f'add {len(rows)=} {all_added=}')
            rows = []
        print(f'fin {all_added=} {all_files=}')
            
    df.reset_index(drop=True).to_feather('database.feather') #17210
    
files_to_df()