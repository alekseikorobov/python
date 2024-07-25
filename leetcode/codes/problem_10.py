

from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def isMatch(self, s: str, p: str) -> bool:
    #     isResult = False
    #     index = 0
    #     index_char = 0
    #     next_char = ''
    #     isMove = False
    #     for c in s:
    #         if len(p)-1 < index:
    #             return False

    #         if len(p)-1 < index + 1:
    #             next_char = p[index + 1]

    #         _p = p[index]
    #         if _p == '.':
    #             isResult = True
    #             isMove = True
    #             index += 1
    #         elif _p == '*':
    #             isResult = True                
    #             isMove = False
    #         elif _p == c and next_char == '':
    #             isResult = True
    #             index += 1
    #             isMove = True
    #         elif _p == c and next_char == '*':
    #             isResult = True
    #             #index += 1
    #             isMove = False
    #         else:
    #             isResult = False
    #             isMove = True
    #         index_char += 1

    #     if isMove:
    #         if len(p) > index:            
    #             index += 1
    #         if index_char < index:
    #             isResult = False
    #     return isResult

        for _p in p:
            print(_p)




s = Solution()

#print(s.isMatch("aab","c*a*b"))
print('a'[0] in {'bb'[0], '.'})