#%%

from typing import List


# class Solution:
#     def isValid(self, s: str) -> bool:
#         last_start_char = ''        
#         for c in s:
#             if c == '(': last_start_char += c
#             elif c == '[': last_start_char += c
#             elif c == '{':  last_start_char += c

#             if(len(last_start_char)>0):
#                 if c == ')' and last_start_char[-1] == '(': 
#                     last_start_char = last_start_char[:-1]
#                 elif c == ']' and last_start_char[-1] == '[':
#                     last_start_char = last_start_char[:-1]
#                 elif c == '}' and last_start_char[-1] == '{':
#                     last_start_char = last_start_char[:-1]
#             else:
#                 return False

#         return len(last_start_char) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        map_c = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            if len(stack)>0:
                if c in ')]}':
                    if stack[-1] == map_c[c]:
                        stack.pop()
                    else:
                        return False
            else:
                return False

        return len(stack) == 0

            
            
    


s = Solution()


print(s.isValid("(])") == True)

# print(s.isValid('(])') == False)

# print(s.isValid('(((()())))') == True)
# print(s.isValid('([') == False)
# print(s.isValid('()[]{}') == True)
# print(s.isValid('(]') == False)

# print(s.isValid("{[]}") == True)

# print(s.isValid("{[]}{") == False)

# print(s.isValid("[{]}") == False)

# print(s.isValid("]") == False)