import os,sys

line = '1'*1024

# 20gb = 20 * 1024mb * 1024kb * 1024b = 21474836480 b
# line 21474836480/1024b = 20_971_520

with open('data.csv','w') as f:
    f.write(f'id,text\n')
    for i in range(20_971_520):
        f.write(f'{i},{line}\n')


#10 - 10038
#100 - 100389
print(f'{os.path.getsize("data.csv")} byte')