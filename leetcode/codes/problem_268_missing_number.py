

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {i:i for i in range(0,len(nums)+1)}
        for n in nums:
            del d[n]
        return list(d.keys())[0]
    
#O(N)
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = [i for i in range(0,len(nums)+1)]
        for n in nums:
            d[n] = -1
        return [r for r in d if r !=-1][0]
#O(N)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = set([i for i in range(0,len(nums)+1)]) - set(nums)
        return next(iter(num))
    
#после просмотра решения
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = sum([i for i in range(0,len(nums)+1)]) - sum(nums)
        return num

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = sum([i - n for i, n in enumerate(nums+[0])])
        return num