from typing import List

class Solution:
    
    def bin(self,arr,t):
        l = 0
        r = len(arr) - 1
        m = -1
        while l <= r:
            m = (r - l)//2 + l            
            if arr[m] == t:
                return (m,0)
            elif arr[m] > t:
                r = m-1
            elif arr[m] < t:
                l = m+1
        
        if l<=r:
            if abs(arr[l]-t) <= abs(arr[m]-t):
                return (l,1)
            else:
                return (m,3)
        else:
            if abs(arr[r]-t) <= abs(arr[m]-t):
                return (r,2)
            else:
                return (m,3)
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return []
    
    
s = Solution()
# print(s.bin([1,2,3],0))
# print(s.bin([1,2,3],1))
# print(s.bin([1,2,3],2))
# print(s.bin([1,2,3],3))
#print(s.bin([1,2,3,150],4))
print(s.bin([1,2,4,150],3))
#print(s.bin([1,2,3,10,20,30,150],149))

# for i in range(1,100):
#     m = list(range(1,i+1))
#     assert s.bin(m,i) == (i-1,0),f'{m} {i}'


# print(s.bin([1,2,3,4],0))
# print(s.bin([1,2,3,4],1))
# print(s.bin([1,2,3,4],2))
# print(s.bin([1,2,3,4],3))
# print(s.bin([1,2,3,4],4))
# print(s.bin([1,2,3,4],5))