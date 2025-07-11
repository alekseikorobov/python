class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        N = len(nums)
        crit = N / 2

        nums = sorted(nums) #NlogN

        curr_max = nums[0]
        count = 1
        for i in range(1,N):
            if nums[i] == curr_max:
                count += 1
                if count > crit:
                    return curr_max
            else:
                curr_max = nums[i]
                count = 1
        return curr_max

#NlogN + N, mem=O(1)
        