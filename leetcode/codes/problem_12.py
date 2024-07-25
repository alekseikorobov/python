

from typing import List


class Solution:
    def __init__(self) -> None:
        self.r = ['','I','II','III']
        self.i1 = 'I'
        self.i5 = 'V'
        self.i10 = 'X'
        self.i50 = 'L'
        self.i100 = 'C'
        self.i500 = 'D'
        self.i1000 = 'M'
        #exception
        #I can be placed before V (5) and X (10) to make 4 and 9. 
        #X can be placed before L (50) and C (100) to make 40 and 90. 
        #C can be placed before D (500) and M (1000) to make 400 and 900.

    def intToRoman(self, num: int) -> str:
        if num < 5:
            if num == 4:
                return  self.i1 + self.i5
            return self.i1 * num
        elif num < 10:
            if num == 9:
                return  self.i1 + self.i10
            return self.i5 + (self.i1 * (num-5))
        elif num < 40:
            return self.i10 * (num // 10) + self.intToRoman(num % 10)
        elif num < 50:
            return self.i10 + self.i50 + self.intToRoman(num % 10)
        elif num < 90:
            return self.i50 + self.i10 * ((num // 10)-5)  + self.intToRoman(num % 10)
        elif num < 100: #XC
            return self.i10 + self.i100 + self.intToRoman(num - 90)
        elif num < 400:
            return self.i100 * (num // 100) + self.intToRoman(num  % 100)
        elif num < 500:
            return self.i100 + self.i500 + self.intToRoman(num  % 100)
        elif num < 900:
            return self.i500 + self.i100 * ((num // 100)-5) + self.intToRoman(num  % 100)
        elif num < 1000: #CM
            return self.i100 + self.i1000 + self.intToRoman(num  % 100)
        elif num < 4000: #CM
            return self.i1000 * (num // 1000) + self.intToRoman(num  % 1000)
                
        #if num > 10:


        


        return ''



s = Solution()

s.intToRoman(1)