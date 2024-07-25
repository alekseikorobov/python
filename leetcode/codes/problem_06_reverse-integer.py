

from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        negative = x < 0
        
        rev_str = ('-' if negative else '') +  s[::-1]
        #print(rev_str)
        rev_int = int(rev_str)

        if (rev_int > ((2**31) - 1)) or (rev_int < -((2**31) - 1)):
            rev_int = 0
        
        return rev_int




s = Solution()

print('123->321', s.reverse(123) )
print('-123->-321', s.reverse(-123) )
print('120->21', s.reverse(120) )