test = True
#test = False

if not test:
    i = input()
else:
    i = '10 2 2 10'

i_m = i.split(' ')
a1 = int(i_m[0])
b1 = int(i_m[1])
a2 = int(i_m[2])
b2 = int(i_m[3])

dic1 = {'a1':a1, 'b1': b1}
dic2 = {'a2':a2, 'b2': b2}
print('dic1',dic1)
print('dic2',dic2)
list_s = []


# p1 = a1 * b1
# p2 = a2 * b2
for b1 in dic1:
    for b2 in dic2:
        for a1 in dic1:
            for a2 in dic2:
                if a1 != b1:
                    if dic1[b1] > dic2[b2]:
                        b_max = b1:
                    else: 
                        b_max = b2:
                    print(a1,'+',a2,b1, (dic1[a1] + dic2[a2],dic1[b1]),'=',(dic1[a1] + dic2[a2])*dic1[b1] )
                    list_s.append((dic1[a1] + dic2[a2],dic1[b1]))

min_p = list_s[0][0]*list_s[0][1]
for a,b in list_s:
    p = a * b
    if p < min_p :
        min_p = p
        print(a, b,'=',a * b)

# if p1 == p2:
#     print(a1 + a2, b1)
#     print(a2, b1*a1)
#     print(b1*a2,b2)
#     print(a1,b1*a2)

# max_side1 = max(a1,b1)
# max_side2 = max(a2,b2)

