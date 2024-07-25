

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = sorted(nums)

        res = 1
        
        for n in nums:
            if n <= 0: continue

            if n == res:
                res += 1

        return res





s = Solution()

print(f'{s.firstMissingPositive(nums = [-1,0,-2])}, 1')

print(f'{s.firstMissingPositive(nums = [1,2,0])}, 3')
