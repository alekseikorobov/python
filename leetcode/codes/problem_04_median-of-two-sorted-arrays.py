

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if nums1 is None:
            return 0.0
        if nums2 is None:
            return 0.0
        nums1.extend(nums2)
        nums1.sort()

        l = len(nums1)

        if l == 0: return 0
        if l == 1: return nums1[0]
        if l == 2: return (nums1[0] + nums1[1]) / 2

        if l % 2 != 0:
            return float(nums1[(l // 2)])
        else:
            i1 = nums1[int((l / 2) - 1)]
            i2 = nums1[int((l / 2))]
            return (i1+i2)/2



s = Solution()

print('[1,3] [2] -> 2, fuct: ',s.findMedianSortedArrays([1,3],[2]))

print('[1,3] [2,4] -> 2, fuct: ',s.findMedianSortedArrays([1,3],[2,4]))

print('[] [] -> 0, fuct: ',s.findMedianSortedArrays([],[]))

print('[] None -> 2, fuct: ',s.findMedianSortedArrays([],None))

print('[1] [] -> 1, fuct: ',s.findMedianSortedArrays([1],[]))

print('[] [1] -> 0, fuct: ',s.findMedianSortedArrays([],[1]))

print('[1] [1] -> 0, fuct: ',s.findMedianSortedArrays([1],[1]))