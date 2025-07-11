class NumArray:

    def __init__(self, nums: List[int]):
        #self.nums = nums
        self.ps = [0] * (len(nums)+1)
        for i in range(0,len(nums)):
            self.ps[i+1]=nums[i]+self.ps[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right+1] - self.ps[left] #sum(self.nums[left:right+1])