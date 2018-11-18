vk = open('txt\\vk.txt','r')

for i in vk.readlines():
    m = i.split('\t')
    print(m[0],m[1].replace('\n',''))