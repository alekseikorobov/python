class Solution:
    def isHappy(self, n: int) -> bool:
        max_count = 1_000_000
        count = 0
        while count < max_count:
            n = sum([x*x for x in map(int,str(n))])
            if n in [4, 9]: return False
            if n == 1: return True
            count+=1
        return False

#O(1_000_000)

# после того как посмотре ответ
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(n):
            res = 0
            while n:
                d = n % 10
                res += d * d
                n = n // 10
            return res
        
        visit = set()
        while n not in visit:
            visit.add(n)
            n = get_next_number(n)            
            if n == 1:
                return True
        return False