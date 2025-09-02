file_result = 'files_20210804.csv'

file_result_duble = 'files_20210804_duble.csv'


with open(file_result,'r') as f:
    lines = f.readlines()
    dictfile = {}
    for i in range(0,len(lines)):
        str = lines[i].replace('\n','')
        splite = str.split('|')
        hash = splite[-1]
        if hash in dictfile:
            dictfile[hash].append(splite[0:-1])
            #break;
        else:
            dictfile[hash] = [splite[0:-1]]

print(len(dictfile))
list_result = []
for key in dictfile:
    if len(dictfile[key])>1:
        for l in dictfile[key]:
            s = '|'.join([key,'|'.join(l)])
            #print(l)
            list_result.append(s)
print(len(list_result))

#save result
with open(file_result_duble,'w') as file:
    for item in list_result:
        file.write("%s\n" % item)