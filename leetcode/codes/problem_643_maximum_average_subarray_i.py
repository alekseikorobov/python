class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ps = [0] * (len(nums)+1)
        for i in range(len(nums)):
            ps[i+1] = nums[i] + ps[i]

        l = len(ps)
        max_avg = float('-inf')
        for i in range(len(ps)):
            a = k + i
            if a>=l:break
            s = ps[a] - ps[i]
            avg = s/k
            if avg>max_avg:
                max_avg = avg
        return max_avg
    
#O(2N)