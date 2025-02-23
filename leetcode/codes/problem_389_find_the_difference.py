
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        t1 = {k:0 for k in 'qwertyuiopasdfghjklzxcvbnm'}
        t2 = t1.copy()
        for c in s:
            t1[c] += 1
        for c in t:
            t2[c] += 1
        
        for t in t1:
            if t1[t] != t2[t]:
                return t

#O(N+M+26)