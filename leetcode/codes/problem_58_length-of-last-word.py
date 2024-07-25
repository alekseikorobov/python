from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        ws = s.split(' ')
        return len(ws[-1])


s = Solution()

print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))

