from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        while N > 0:
            n = nums[i]
            #print('n in nums[0:i]',n in nums[0:i], n,nums[0:i])
            if i > 0 and n in nums[0:i]:
                nums.pop(i)
                #N += 1
                i -= 1
            N -= 1
            i += 1
        return len(nums)



s = Solution()

n = [1,1,2]
print(s.removeDuplicates(n),n)

n = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(n),n)