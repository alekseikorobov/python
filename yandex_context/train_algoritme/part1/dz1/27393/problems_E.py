

#K - квартира
#P - подъезд
#N - этаж
def get_count_kv_on_f(K2,M,P2):
    for i in range(1,100):
        f_n = (K2-1) // i # индекс этажа
        P_fact = f_n//M + 1 # предполагаемый норме подъезда
        if P_fact == P2: # если предполагаемый равен фактическу, тогда считаем его истинным
            return i
    return 0
        
def solve(K1:int, M:int, K2:int, P2:int, N2:int):
    
    #f = K2 // N2 + 1 # получаем сколько квартир на этаже
    
    # получяем номер этажа
    num_kv = get_count_kv_on_f(K2,M,P2)
    print(num_kv)
    

    return 0,0
	


if __name__ == '__main__':
    is_test = True
    v  = '10 3 15 2 2' if is_test else input()
    
    
    K1, M, K2, P2, N2 = map(int,v.split())

    P1,N1 = solve(K1, M, K2, P2, N2)
    print(P1,N1)



