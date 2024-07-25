from typing import List


class Solution:

    def fact(self,n):
        if n == 0: return 1
        return n * self.fact(n - 1)

    def f(self, n , x):
        print(f'{n=} {x=}')
        l = (-1.0**n) * 2.0 * self.fact(n)
        print(f'    {l=}')
        r = (1.0 - (2.0*n)) * (self.fact(n)**2.0)  * (4.0**n)
        print(f'    {r=}')
        p1 = l * (x ** n)
        print(f'{p1=}')
        return (p1/r)

    # def mySqrt(self, x: int) -> int:
    #     x -= 1.
    #     q = 1.
    #     sum = 1.
    #     for n in range(1,2):
    #         q *= (-1.0) * ((2. * n) - 1) * 2. * n * x / (n * n * 4)
    #         sum += q / (1.0 - (2 * n))        
    #     return sum
    

    def mySqrt_(self, x: int) -> int:
        #x += 1
        res = 1
        for i in range(1,10):
            print(res)
            res += self.f(i,x-1)
        
        return int(res)
    
    def mySqrt(self, x: int) -> int:
        xn = x;
        while True:
            if xn == 0: break
            xn_1 = (xn + x/xn) / 2
            if xn == xn_1: break
            xn = xn_1
        return int(xn)

s = Solution()

# print(s.fact(1)) #1
# print(s.fact(2)) #2
# print(s.fact(3)) #6
# print(s.fact(4)) #24
# print(s.fact(5)) #120
# print(s.fact(6)) #720

#print(s.mySqrt(4))
print(s.mySqrt(2147395599)) #46339