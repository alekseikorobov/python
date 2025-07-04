test = True
side = []
if not test:
    side.append(int(input()))
    side.append(int(input()))
    side.append(int(input()))
else:
    side = [3,5,4]
    side = [1,1,1]
    # side = [0,1,1]
    # side = [1,0,1]
    # side = [1,1,0]
    # side = [1,1,-1]
    # side = [10000,1,1]
    # side = [10000,10000,1]
    #side = [10000,500,1]
    side = [1,1,2]
    side = [2,2,4]

exists = True
for i_a in range(3):
    for i_b in range(3):
        for i_c in range(3):
            if i_a != i_b and i_a != i_c and i_b != i_c:
                a = side[i_a]                
                b = side[i_b]
                c = side[i_c]
                if a <= 0 or b <= 0 or c <= 0:
                    exists = False
                    break
                if a + b <= c:
                    print(a, b, c)
                    exists = False

if exists:
    print('YES')
else:
    print('NO')