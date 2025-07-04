#За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E. Замок Иф сложен из кирпичей, размером A × B × C. Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие, если стороны кирпича должны быть параллельны сторонам отверстия.

#Формат ввода
#Программа получает на вход числа A, B, C, D, E.

#Формат вывода
#Программа должна вывести слово YES или NO.


test = False

def ans(a,b,c,d,e):
    
    if a <=0: a = 0
    if b <=0: b = 0
    if c <=0: c = 0
    if d <=0: d = 0
    if e <=0: e = 0
    
    p_will_min = min(a * b, min(a * c,b * c) )
    #print('p_will_min',p_will_min)
    p_hole = d * e
    if p_hole >= p_will_min:
        return 'YES'
    else:
        return 'NO'

if not test:
    a,b,c,d,e = int(input()), int(input()), int(input()), int(input()), int(input())
    print(ans(a,b,c,d,e))
else:
    l_tests = [
        ((1,1,1,1,1),'YES'),
        ((2,2,2,1,1),'NO'),
        ((2,2,2,0,0),'NO'),
        ((0,0,0,1,1),'YES'),
        ((2,2,2,-1,-1),'NO'),
        ((-2,-2,-2,2,2),'YES'),
        ((1,2,3,1,1),'NO'),
        ((1,2,3,2,1),'YES'),
        ((1,2,3,1,3),'YES'),
        ((1,2,300,1,3),'YES'),
        ((1,200,3,1,3),'YES'),
        ((100,2,3,1,3),'NO'),
        ]
    for args, resp in l_tests:
        a,b,c,d,e = args
        r = ans(a,b,c,d,e)
        if r != resp: 
            print('error ',args,'=',r, ' must be =',resp)