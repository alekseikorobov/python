
#%%
import pandas as pd

df = pd.read_feather('/home/aleksei/MyProject/python/database.feather')
df['timePublished_dt'] = pd.to_datetime(df['timePublished'])
df = df[df['timePublished_dt'].notna()]

# %%
#df.info()
# %%
#df[(df['author_fullname'].notna()) & (df['author_fullname'].str.contains('korob'))]


#df[(df['titleHtml'].notna()) & (df['titleHtml'].str.contains('менеджер'))]

#%%


#%%

df['timePublished_dt'].dt.year.value_counts().sort_index().plot(kind='bar')

#%%

df['timePublished_dt'].dt.month.value_counts().sort_index().plot(kind='bar')
#%%

df.set_index('timePublished_dt')['statistics_commentsCount'].plot()
#%%
df.sort_values('statistics_commentsCount',ascending=False).head(10)

#%%
df.set_index('timePublished_dt')['statistics_favoritesCount'].plot()

#%%

df.sort_values('statistics_favoritesCount',ascending=False).head(10)

#%%
df.set_index('timePublished_dt')['statistics_votesCountPlus'].plot()
#%%
#pd.options.display.width = 200
#pd.options.display.max_colwidth = 200
#pd.options.display.max_columns=100
#pd.options.display.min_rows=100
#%%

df[df['statistics_votesCountPlus'] != 32767.0].sort_values('statistics_votesCountPlus',ascending=False)[['id','statistics_votesCountPlus','titleHtml','timePublished_dt']].head(10)
#%%
df[df['statistics_votesCountPlus'] != 32767.0].set_index('timePublished_dt')['statistics_votesCountPlus'].plot()


#%%
df.set_index('timePublished_dt')['statistics_readingCount'].plot()

#%%

df.sort_values('statistics_readingCount',ascending=False)[['id','statistics_readingCount','titleHtml','timePublished_dt']].head(100)

