from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        incriment = 5
        if len(digits) == 0: return [incriment]
        
        for n in range(len(digits)-1,-1,-1):
            digits[n] += incriment
            incriment = int(digits[n] / 10)
            if digits[n] > 9:
                digits[n] = digits[n] % 10
            if n == 0 and incriment>0:
               digits.insert(0,incriment)
        return digits

s = Solution()

print(s.plusOne([]))
print(s.plusOne([1]))
print(s.plusOne([1,2,3]))
print(s.plusOne([1,9,9,9]))
print(s.plusOne([9,9,9]))

