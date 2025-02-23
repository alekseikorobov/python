class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #1.
        #return list(set(nums1) & set(nums2))
        
        #2.
        # result = []
        # for n1 in nums1:
        #     for n2 in nums2:
        #         if n1 == n2 and n1 not in result:
        #             result.append(n1)
        # return result

        # a = 0
        # b = 0
        # n_a, n_b = len(nums1),len(nums2)
        # result = set()
        # result.add(nums1[a])
        # result_l = []
        # while a < n_a and b < n_a:
        #     if nums2[b] in result:
        #         if nums2[b] in result_l:
        #             result_l.append(nums2[b])
        #         b += 1
        #     else:

        res = {}
        for n in nums1:
            res[n] = 1
        for n2 in nums2:
            if n2 in res:
                res[n2] += 1
        return [k for k,v in res.items() if v>1]


#O(N+M)