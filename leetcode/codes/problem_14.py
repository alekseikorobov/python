

from typing import List
from collections import Counter

class Solution:
    def __init__(self) -> None:
        pass
    

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<2:
            return strs[0]

        min_len = min([len(w) for w in strs])

        result = ''
        for ng in range(min_len,0,-1):
            substrs = set([w[0:ng] for w in strs])
            if len(substrs) == 1:
                result = list(substrs)[0]
                break
        return result


s = Solution()

#s.longestCommonPrefix(['12','456','789'])
#s.longestCommonPrefix(['123','456','789'])
print(s.longestCommonPrefix(['a']))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["ab", "a"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["reflower","flow","flight"]))

