class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # медленное решение
        # store = set()
        # for n in nums:
        #     if n in store:
        #         return True
        #     store.add(n)
        # return False

        # самое быстрое решение
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

#O(NlogN + N)