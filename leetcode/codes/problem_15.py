

from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def twoSum(self, nums: List[int]) -> List[List[int]]:
        res = [0]*(len(nums)+1)
        print(nums)
        for i in range(1,len(nums)-1):
            res[i] += res[i-1] + nums[i - 1]
        
        print(res)

        # N = len(nums)
        # if N < 2:
        #     return []
        # nums = sorted(nums)
        # #a,b,c = 0,1,2
        # res = []
        # for a in range(0, N):
            
        #     if nums[a] > 0: break;

        #     for b in range(a + 1, N):
        #         if nums[a] != -nums[b]:
        #             break
        # return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        #print(nums)
        N = len(nums)
        result = []

        for num1idx in range(0,N):
            if num1idx > 0 and nums[num1idx] == nums[num1idx - 1]:
                continue

            num2idx = num1idx + 1
            num3idx = N - 1
            while num2idx < num3idx:
                sum = nums[num1idx] + nums[num2idx] + nums[num3idx]
                if sum < 0:
                    num2idx += 1
                elif sum > 0:
                    num3idx -= 1    
                elif sum == 0:# and num3idx+1 < N and nums[num3idx] != nums[num3idx+1]:
                    result.append([nums[num1idx],nums[num2idx],nums[num3idx]])
                    num3idx -= 1
                    while num2idx < num3idx and nums[num3idx] == nums[num3idx + 1]:
                        num3idx -= 1        
        return result


    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        print(nums)
        N = len(nums)
        res = []
        iter = 0
        for a in range(0, N):
            b0 = a + 1
            if nums[a] > 0:
                break
            if b0 > N and nums[a] + nums[b0] > 0:
                break
            for b in range(a + 1, N):
                if nums[a] + nums[b] > 0:
                    break
                    #return res
                for c in range(b + 1, N):
                    print(a,b,c,'  ', nums[a],nums[b], nums[c], '=' ,nums[a]+nums[b]+nums[c])
                    iter += 1
                    if nums[a] + nums[b] == -nums[c]:                        
                        s = [nums[a],nums[b],nums[c]]
                        isExists = False
                        for l in res:
                            if l == s:
                                isExists = True
                                break
                        if not isExists:
                            res.append(s)
        print(iter)
        return res


    def threeSum_1(self, nums: List[int]) -> List[List[int]]:

        res = []
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if i == j or i == k or k == j:
                        continue
                    if nums[i] > 0 and  nums[j] > 0 and nums[k] > 0: continue 
                    #if nums[i] + nums[k] > 0: continue 
                    #if nums[j] + nums[k] > 0: continue 

                    if nums[i] + nums[j] + nums[k] == 0:
                        #print(i,j,k)
                        s = sorted([nums[i],nums[j],nums[k]])

                        isExists = False
                        for l in res:
                            if l == s:
                                isExists = True
                                break
                        if not isExists:
                            res.append(s)
        return res

s = Solution()
#print(s.threeSum([-1,0,1,2,-1,-4]))
#print(s.threeSum([3,0,-2,-1,1,2])) #[[-2,-1,3],[-2,0,2],[-1,0,1]]
#print(s.threeSum([1,1,-2]))
#print(s.threeSum([82597,-9243,62390,83030,-97960,-26521,-61011,83390]))

#print(s.twoSum([1,-1]))
#print(s.twoSum([-1,0,1,2,-1,-4]))
#print(s.threeSum([-1,0,1,2,-1,-4]))

print(s.threeSum([2,-1,0,-1,1]))



