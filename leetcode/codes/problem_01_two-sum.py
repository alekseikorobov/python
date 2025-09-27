class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for index_a in range(len(nums)):
            for index_b in range(index_a + 1,len(nums)):
                print(index_a,index_b)
                if nums[index_a] == target - nums[index_b]:
                    return [index_a,index_b]
        return [-1,-1]
        
s = Solution()
res = s.twoSum([3,2,4],6)
print(res)

# more optimal
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i
#         # Return an empty list if no solution is found
#         return []