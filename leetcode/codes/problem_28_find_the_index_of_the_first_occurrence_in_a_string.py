#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=problem-list-v2&envId=5zpgt6y1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a,b = 0, 0
        N,N1 = len(haystack), len(needle) 
        while a < N:
            a1 = a
            while a1 < N and b < N1 and haystack[a1] == needle[b]:
                b+=1
                a1+=1
            if b == N1:
                return a
            b = 0
            a += 1
        return -1
    
# O(N*M)