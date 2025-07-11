from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        N = len(candidates)

        res = []

        while i < N:
            part = []
            c = candidates[i]
            ost = target
            
            ost -= c
            if ost > 0:
                

            i += 1

        


        return res
        




s = Solution()

print(f'{s.combinationSum(candidates = [2,3,6,7], target = 7)}, [[2,2,3],[7]]')