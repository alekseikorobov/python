

from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        a = 0
        b = len(s) - 1

        while a < b and s[a] == s[b]:
            a += 1
            if a == b: break
            b -= 1
            
        return a == b
