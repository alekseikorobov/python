

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        last_start_char = ''        
        for c in s:
            if c == '(': last_start_char += c
            elif c == '[': last_start_char += c
            elif c == '{':  last_start_char += c

            if(len(last_start_char)>0):
                if c == ')' and last_start_char[-1] == '(': 
                    last_start_char = last_start_char[:-1]
                elif c == ']' and last_start_char[-1] == '[':
                    last_start_char = last_start_char[:-1]
                elif c == '}' and last_start_char[-1] == '{':
                    last_start_char = last_start_char[:-1]
            else:
                return False

        return len(last_start_char) == 0
    


s = Solution()


print(s.isValid('()') == True)

print(s.isValid('(])') == False)

print(s.isValid('(((()())))') == True)
print(s.isValid('([') == False)
print(s.isValid('()[]{}') == True)
print(s.isValid('(]') == False)

print(s.isValid("{[]}") == True)

print(s.isValid("{[]}{") == False)

print(s.isValid("[{]}") == False)

print(s.isValid("]") == False)