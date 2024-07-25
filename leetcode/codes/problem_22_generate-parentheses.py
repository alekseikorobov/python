

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        if n == 1:
            res.append("()")

        for i in range(1, n):
            part_res = self.generateParenthesis(i)

        return res




s = Solution()
print(s.generateParenthesis(1),["()"])
#print(s.generateParenthesis(2),["(())","()()"])
#print(s.generateParenthesis(3),["((()))","(()())","(())()","()(())","()()()"])