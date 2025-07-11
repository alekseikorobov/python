
#%%
c = [0]*9

c[0] = 'x'
#print(c)

def is_wine(m,xo='x'):
    for y in range(3):
        count = 0
        for x in range(3):
            if xo == m[x+(y*3)]:
                count += 1
        if count == 3:
            return True
        count = 0
        for x in range(3):
            if xo == m[(x * 3) + y]:
                count += 1
        if count == 3:
            return True
        
    if ((xo==m[0] and xo == m[4] and xo == m[8]) \
        or (xo==m[2] and xo == m[4] and xo == m[6])):
        return True
    return False

print(is_wine(['x','x','x',0,0,0,0,0,0]))
print(is_wine([0,0,0,'x','x','x',0,0,0]))
print(is_wine([0,0,0,0,0,0,'x','x','x']))

print(is_wine(['x',0, 0,'x',0,0,'x',0,0]))
print(is_wine([0,'x',0, 0,'x',0,0,'x',0]))
print(is_wine([0,0,'x',0, 0,'x',0,0,'x']))

print(is_wine([0,0,'x',0,'x',0,'x',0,0]))
print(is_wine(['x',0,0,0,'x',0,0,0,'x']))

print()

print(is_wine([0,'x','x','x',0,0,0,0,0]))
print(is_wine([0,'x',0,0,'x','x',0,0,0]))
print(is_wine([0,0,0,0,0,'x',0,'x','x']))

print(is_wine(['x',0, 0,0,0,0,'x',0,0]))
print(is_wine([0,'x',0, 0,'x',0,'x',0,0]))
print(is_wine([0,0,'x',0, 0,'x',0,'x',0]))

print(is_wine([0,0,'x',0,'x',0,0,0,'x']))
print(is_wine(['x',0,0,0,'x',0,0,'x',0]))

print()
print(is_wine(['x','x',0,0,'x','x','x',0,0]))
print(is_wine(['x','x',0,'x',0,'x',0,0,'x','x']))


#%%
import copy

def step_set(c, i, xo):
    c[i] = xo
    return c
    
c = [0]*9

def fill(c,xo,all_steps=[]):
    print(f'start {c=},{xo=},{all_steps=}')
    if 0 in c:
        for i in range(9):
            if i in all_steps: continue
            c1 = step_set(copy.copy(c),i,xo)
            all_steps.append(i)
            print(c1)
            xo = 'x' if xo == 'o' else 'x'
            fill(c1,xo,all_steps)
    #return c1

fill(c,'x')
    

# for i1 in range(9):
#     c = step_set(copy.copy(c),i1,'x')
#     print(c)
#     for i2 in range(9):
#         if i1 == i2: continue
#         c1 = step_set(copy.copy(c),i2,'o')
#         print('\t',c1)
#         for i3 in range(9):
#             if i3 in [i1,i2]: continue
#             c2 = step_set(copy.copy(c1),i3,'x')
#             print('\t\t',c2)
#             for i4 in range(9):
#                 if i4 in [i1,i2,i3]: continue
#                 c3 = step_set(copy.copy(c2),i4,'o')
#                 print('\t\t\t',c3)
#                 for i5 in range(9):
#                     if i5 in [i1,i2,i3,i4]: continue
#                     c4 = step_set(copy.copy(c3),i5,'x')
#                     print('\t\t\t\t',c4)
