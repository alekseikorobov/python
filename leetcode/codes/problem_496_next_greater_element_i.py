class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        store = {}
        l = len(nums2)
        for i in range(l):
            m = -1
            s = i + 1
            while s < l:
                if nums2[s] > nums2[i]:
                    m = nums2[s]
                    break
                s+=1
            store[nums2[i]] = m

        return [store[n] for n in nums1]