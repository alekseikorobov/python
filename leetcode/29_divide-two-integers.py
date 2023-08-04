from typing import Tuple


class Solution:

    def divide_part(self,dividend: int, divisor: int) -> Tuple[int,int]:        
        divisor = divisor
        ost = dividend
        res = 0
        while ost >= divisor:
                ost -= divisor
                res += 1        
        return res, ost
    
            

    def divide(self, dividend: int, divisor: int) -> int:
        print(f'Excepted {int(dividend/divisor)=}')
        is_neg = False if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) else True        
        
        divisor = abs(divisor)
        ost = abs(dividend)
        
        res = 0
        if divisor == 1:
            res = [str(ost)]
        else:
            now_div = ''
            dividend_str = str(ost)
            N = len(dividend_str)
            i = 0
            res = []
            while i < N:                
                now_div += dividend_str[i]                
                while int(now_div) < divisor and i + 1 < N:
                    res.append('0')
                    i += 1
                    now_div += dividend_str[i]
                
                r,s = self.divide_part(int(now_div), divisor)
                #print(f'{r=} {s=}')
                res.append(str(r))

                now_div = str(s)

                i += 1
            pass
        res = int(''.join(res))
        pre_res = -res if is_neg else res

        if pre_res > 2147483647:
            return 2147483647
        elif pre_res < -2147483648:
            return -2147483648
        
        return pre_res





s = Solution()

print(s.divide(10,3))
print(s.divide(7,-3))
print(s.divide(-7,3))
print(s.divide(-7,-3))
print(s.divide(1,1))
print(s.divide(100,1))
print(s.divide(-1,1))
print(s.divide(-2147483648,-1))
print(s.divide(-2147483648,1))
print(s.divide(13,2))
print(s.divide(135,2))

# print(s.divide(2147483647,2))

# print(s.divide(214,2))



# 2147483647 / 2

# 2 = 1
# 14 = 07
# 7 = 3
# 14 = 7
# 8 = 4
# 3 = 1
# 16 = 8
# 4 = 2
# 7 = 3


#print(s.divide(125,2))

# 3,1
# 11
