from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        i = 0
        while N > 0:
            n = nums[i]
            if n == val:
                nums.pop(i)
                i -= 1
            N -= 1
            i += 1
        return len(nums)



s = Solution()

n = [3,2,2,3]
print(s.removeElement(n,3),n)

n = [0,1,2,2,3,0,4,2]
print(s.removeElement(n,2),n)