

from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def romanToInt(self, s: str) -> int:
        result = 0
        previe1 = False
        previe2 = False
        previe3 = False
        for i in range(len(s)-1,-1,-1):
            if s[i] == 'I':
                if previe1:
                    result -= 1
                else:
                    result += 1                
                previe1 = False
            if s[i] == 'V':
                previe1 = True
                result += 5
            if s[i] == 'X':
                if previe2:
                    result -= 10
                else:
                    result += 10
                previe1 = True
                previe2 = False
            if s[i] == 'L':
                previe2 = True
                result += 50
            if s[i] == 'C':
                if previe3:
                    result -= 100
                else:
                    result += 100
                previe2 = True
                previe3 = False
            if s[i] == 'D':
                previe3 = True
                result += 500
            if s[i] == 'M':
                previe3 = True
                result += 1000
        return result


s = Solution()
# print(s.romanToInt('XIII'))
# print(s.romanToInt('VIII'))
# print(s.romanToInt('IV'))
# print(s.romanToInt('XXXIX'))
print(s.romanToInt('XLVIII'))
print(s.romanToInt('LXXXV'))