class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = [0]*len(nums)
        a = 0
        b = len(nums)-1
        index = b
        while a <= b:

            v1 = nums[a]**2
            v2 = nums[b]**2

            if v1 > v2:
                result[index] = v1
                a+=1
            else:
                result[index] = v2
                b-=1
            
            index -= 1
        
        return result