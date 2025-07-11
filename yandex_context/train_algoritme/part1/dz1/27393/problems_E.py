

#K1 - квартира
#K2 - квартира ранее
#P2 - подъезд квартиры K2
#N2 - этаж подъезд P2
#N - этаж

import math

def get_count_kv_on_f(K2,M,P2):
    pass

# def build_house(M, K2, P2, N2):
#     #мы можем начать строить дом с первой квартиры, до последней квартиры K2
#     #главное чтобы во время строительства совпал этаж 
#     # но мы не знаем сколько квартир на одном этаже-
        
    
    
        
def solve(K1:int, M:int, K2:int, P2:int, N2:int):
    
    n_all = (M * (P2-1)) + N2
    count_kv = math.ceil(K2/n_all)
    n1_all = math.ceil(K1/count_kv)
    print(f'{n_all=},{count_kv=},{n1_all=}')
    p1 = math.ceil(n1_all/M)
    if count_kv 
        n1 = n1_all - (M*(p1-1))
    return p1,n1



if __name__ == '__main__':
    is_test = True
    v  = '89 20 41 1 11' if is_test else input()
    v  = '11 1 1 1 1' if is_test else input()
    
    
    K1, M, K2, P2, N2 = map(int,v.split())

    P1,N1 = solve(K1, M, K2, P2, N2)
    print(P1,N1)



