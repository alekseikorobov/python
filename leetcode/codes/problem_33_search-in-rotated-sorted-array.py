class Solution:

    def bin_search(self,nums,target):
        pass

    def search(self, nums: List[int], target: int) -> int:
        min_val = min(nums)
        last_val = nums[-1]
        N = len(nums)
        last_index = N-1
        k = last_index - last_val + min_val

        repair_nums = [*nums[k:],*nums[0:k]]
        index = self.bin_search(repair_nums)
        return index + k
