class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l,f = 0,0
        N = len(nums)
        while f < N:
            if nums[f] != 0:
                nums[l] = nums[f]
                l += 1
            f+=1
        for i in range(l,N):
            nums[i] = 0

#O(N)