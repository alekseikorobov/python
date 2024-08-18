

def round_to_next(n):
    if n == 0:
        return 0
    ost = n % 5
    if ost == 0:
        return n
    p = 5 - ost
    return n+p
    

print(f'{round_to_next(0)=}')
print(f'{round_to_next(1)=}')
print(f'{round_to_next(2)=}')
print(f'{round_to_next(3)=}')
print(f'{round_to_next(4)=}')
print(f'{round_to_next(5)=}')
print(f'{round_to_next(6)=}')
print(f'{round_to_next(7)=}')
print(f'{round_to_next(10)=}')
print(f'{round_to_next(11)=}')
print(f'{round_to_next(22)=}')
