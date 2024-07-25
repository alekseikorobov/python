

from typing import List


class Solution:
    def __init__(self) -> None:
        pass
    # def maxArea(self, height: List[int]) -> int:
        
    #     s_max = 0

    #     for i in range(0,len(height)):
    #         for j in range(i+1,len(height)):
    #             _min = min(height[i],height[j])                
                
    #             s = _min * (j - i)

    #             if s > s_max:
    #                 s_max = s

    #     return s_max

#         for i in range(0,len(height)):
#             for j in range(i+1,len(height)):
#                 _min = min(height[i],height[j])                
                
#                 s = _min * (j - i)

#                 if s > s_max:
#                     s_max = s

#         return s_max
    def maxArea(self, height: List[int]) -> int:
        s_max = 0
        l = 0
        r = len(height) - 1
        while l < r:
            m = min(height[l], height[r]) * (r - l)
            if m > s_max:
                s_max = m
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return s_max


s = Solution()
# print(s.maxArea([]))
# print(s.maxArea([1]))
# print(s.maxArea([1,1]))
# print(s.maxArea([5,5]))
# print(s.maxArea([5,6]))
# print(s.maxArea([5,4]))

#print(s.maxArea([1,2, 1]))

#print(s.maxArea([1,2, 3]))
#print(s.maxArea([1,2, 3]))
# print(s.maxArea([1,2, 3, 4]))

# print(s.maxArea([1,2, 3, 2, 1]))
# print(s.maxArea([2,3,4,5,18,17,6]))
# print(s.maxArea([1,2,3,4,5,25,24,3,4]))
#print(s.maxArea([4,4,2,11,0,11,5,11,13,8]))

#14091 #15423
print(s.maxArea([159,157,139,51,98,71,4,125,48,125,64,4,105,79,136,169,113,13,95,88,190,5,148,17,152,20,196,141,35,42,188,147,199,127,198,49,150,154,175,199,80,191,3,137,22,92,58,87,57,153,175,199,110,75,16,62,96,12,3,83,55,144,30,6,23,28,56,174,183,183,173,15,126,128,104,148,172,163,35,181,68,162,181,179,37,197,193,85,10,197,169,17,141,199,175,164,180,183,90,115]))