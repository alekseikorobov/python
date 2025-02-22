class Solution:

    def get_ps(self,nums):
        ps = [0]*(len(nums)+1)
        for i in range(0,len(nums)):
            ps[i+1] = ps[i] + nums[i]
        return ps

    def pivotIndex(self, nums: List[int]) -> int:
        ps = self.get_ps(nums)
        N = len(nums)
        for i in range(N):
            l1,r1 = 0, i
            l2,r2 = i+1,N-1
            left_sum = ps[r1] - ps[l1]
            right_sum = ps[r2+1] - ps[l2]
            if left_sum == right_sum:
                return i
        return -1
