test = True
#test = False

if not test:
    a = int(input())
    b = int(input())
    c = int(input())
else:
    a,b,c = 1,0,0
    #a,b,c = 1,2,3
    #a,b,c = 1,2,-3
    #a,b,c = 2,2,3
    #a,b,c = 0,9,3
    a,b,c = 1,9,3

if c < 0:
    print('NO SOLUTION')

if a  == 0:
    print('MANY SOLUTIONS')
else:
    x = ((c**2) - b) / a

    if (a * x) + b < 0:
        print('MANY SOLUTIONS')

    if x.is_integer():
        print(int(x))
    else:
        print('NO SOLUTION')