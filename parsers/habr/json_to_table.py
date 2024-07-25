#перевод статей из json файлов в таблицу pandas DataFrame

import os,json
import pandas as pd

BASE_DIR = 'data'

df = pd.DataFrame()

def get_date_from_schemaJsonLd(json_str):
    obj = json.loads(json_str)
    return obj['dateModified'],obj['datePublished']
    
keys = ['id', 'timePublished', 'isCorporative', 'lang', 'titleHtml', 'leadData', 'editorVersion', 'postType', 'postLabels', 'author', 'statistics', 'hubs', 'flows', 'relatedData', 'textHtml', 'tags', 'metadata', 'polls', 'commentsEnabled', 'rulesRemindEnabled', 'votesEnabled', 'status', 'plannedPublishTime', 'checked', 'hasPinnedComments', 'format', 'banner', 'multiwidget', 'readingTime', 'complexity', 'isEditorial']
def file_to_df(path):
    with open(path,'r') as f:
        res = json.load(f)
        if 'httpCode' in res:
            print(f'{res["httpCode"]=}')            
        else:
            dateModified,datePublished = get_date_from_schemaJsonLd(res['metadata']['schemaJsonLd'])            
            row = {
                'id':res['id'],
                'timePublished':res['timePublished'],
                'isCorporative':res['isCorporative'],
                'lang':res['lang'],
                'titleHtml':res['titleHtml'],
                'postType':res['postType'],
                #'postLabels':res['postLabels'], список пустой
                'author_id':res['author']['id'],
                'author_alias':res['author']['alias'],
                'author_fullname':res['author']['fullname'],
                'statistics_commentsCount':res['statistics']['commentsCount'],
                'statistics_favoritesCount':res['statistics']['favoritesCount'],
                'statistics_readingCount':res['statistics']['readingCount'],
                'statistics_score':res['statistics']['score'],
                'statistics_votesCount':res['statistics']['votesCount'],
                'statistics_votesCountPlus':res['statistics']['votesCountPlus'],
                'statistics_votesCountMinus':res['statistics']['votesCountMinus'],
                'hubs':';'.join(i['titleHtml'] for i in res['hubs']),
                'flows':';'.join(i['titleHtml'] for i in res['flows']),
                #'relatedData':res['relatedData'], #value none!!!!
                'textHtml_len':len(res['textHtml']),
                #'textHtml_count_words':get_count_words_from_str(res['textHtml']),
                'tags':';'.join(i['titleHtml'] for i in res['tags']),
                'metadata_dateModified':dateModified,
                'metadata_datePublished':datePublished,
                #'polls':res['polls'], список пустой
                'commentsEnabled_status':res['commentsEnabled']['status'],
                'commentsEnabled_reason':res['commentsEnabled']['reason']
                ,'rulesRemindEnabled':res['rulesRemindEnabled']
                ,'votesEnabled':res['votesEnabled']
                ,'status': res['status']
                #,'plannedPublishTime':res['plannedPublishTime'] #value none!!!!
                #,'checked':res['checked'] #value none!!!!
                ,'hasPinnedComments':res['hasPinnedComments']
                #,'format':res['format'] #value none!!!!
                #,'banner':res['banner'] #value none!!!!
                #,'multiwidget':res['multiwidget'] #value none!!!!
                ,'readingTime':res['readingTime']
                #,'complexity':res['complexity'] #value none!!!!
                ,'isEditorial':res['isEditorial']
            }
            
            #print(res.keys())
            # for k in keys:
            #     val = res[k]
            #     if type(val) is str:
            #         print(f'{k=}, {len(res[k])}')
            #     else:
            #         print(f'{k=}, not str {type(val)=}, {val=}')
            
        

path = '/home/aleksei/MyProject/python/parsers/habr/data/data_3/articles_60011.json'
path = '/home/aleksei/MyProject/python/parsers/habr/data/data_3/articles_60007.json'
file_to_df(path)

# for root,dirs,files in os.walk(BASE_DIR):
#     for file in files:
#         path = os.path.join(root,file)
#         file_to_df(path)
        
    