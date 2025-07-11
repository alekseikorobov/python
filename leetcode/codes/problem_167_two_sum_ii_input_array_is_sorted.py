
# такая же задача как и problem_01_two-sum.py, но более сложные проверки!

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def bin_search(sub_numbers,l,r,t):
            while l <= r:
                m = (r-l//2) + l
                if sub_numbers[m] == t:
                    return m
                elif t < sub_numbers[m]:
                    r = m - 1
                    return bin_search(sub_numbers,l,r,t)
                elif t > sub_numbers[m]:
                    l = m + 1
                    return bin_search(sub_numbers,l,r,t)
            return -1

        visit=set()
        for i in range(0,len(numbers)):
            if numbers[i] in visit:
                continue
            t1 = target - numbers[i]
            sub_numbers = numbers[i:len(numbers)]
            
            j = bin_search(sub_numbers,0,len(sub_numbers)-1,t1)
            if j != -1:
                return [i+1,j+i+1]
            
            visit.add(numbers[i])

#O(NLogN) * O(N)
# из видео - https://www.youtube.com/watch?v=6h-blOjL43s
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers)-1
        while a < b:
            s = numbers[a] + numbers[b]
            if s < target:
                a+=1
            elif s > target:
                b -= 1
            else:
                return [a+1,b+1]
            
#O(N)
            
# и если массив не отсортирован
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        N = len(numbers)
        h = {numbers[0]:0}
        a = 1
        while a < N:
            diff = target - numbers[a]
            if diff in h:
                return [h[diff]+1,a+1]
            h[numbers[a]] = a
            a += 1
        return False
#O(N)