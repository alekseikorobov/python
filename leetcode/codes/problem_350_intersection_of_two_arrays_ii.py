class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        for n in nums1:
            if n not in store:
                store[n] = 1
            else:
                store[n] += 1
        
        result = []
        for n in nums2:
            if n in store and store[n]>0:
                store[n] -= 1
                result.append(n)
        return result
    
    
# решение после просмотра ответа:
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n_a,n_b = len(nums1),len(nums2)
        a,b = 0,0
        result = []
        while a < n_a and b < n_b:
            if nums1[a] < nums2[b]:
                a += 1
            elif nums1[a] > nums2[b]:
                b += 1
            else:
                result.append(nums1[a])
                a += 1
                b += 1
        return result