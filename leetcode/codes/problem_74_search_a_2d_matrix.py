from typing import List

class Solution:
    def __init__(self):
        self.deep = 0
    
    def searchArray(self, m: List[int], target: int) -> bool:
        self.deep += 1
        #print(f'{self.deep=}')
        l, r = 0,len(m)
        while l < r:
            mid_index = (r - l) // 2
            #print(f'{mid_index=}, {m[l:r]}')
            if m[mid_index] > target:
                r = mid_index
                return self.searchArray(m[l:r],target)
            elif m[mid_index] < target:                
                l = mid_index+1
                return self.searchArray(m[l:r],target)
            else:
                return True
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #work
        #return self.searchMatrix_v1(matrix,target)
        #work
        #return self.searchMatrix_v2(matrix,target)
        
        return self.searchMatrix_v3(matrix,target)
    
    def searchMatrix_v1(self, matrix: List[List[int]], target: int) -> bool:
        for a in matrix:
            res = self.searchArray(a,target)
            if res:
                return True
        return False    
        
    def searchMatrix_v2(self, matrix: List[List[int]], target: int) -> bool:        
        array = []
        for m in matrix:
            array.extend(m)
        return self.searchArray(array,target)

    # def searchArray_v2(self, matrix: List[List[int]], target: int) -> bool:
    #     self.deep += 1
    #     #print(f'{self.deep=}')
               
    #     l_i,l_j = 0,0
    #     r_i,r_j = len(matrix[0]),len(matrix)
        
    #     while l < r:
    #         mid_index_i = (r_i - l_i) // 2
    #         mid_index_j = (r_j - l_j) // 2
    #         #print(f'{mid_index=}, {m[l:r]}')
    #         if matrix[mid_index_i,mid_index_j] > target:
    #             r_i = matrix[mid_index_i]
    #             r_j = matrix[mid_index_j]
    #             return self.searchArray(
    #                 [
    #                     m for m in range()
    #                 ]
    #                 ,target)
    #         elif m[mid_index] < target:                
    #             l = mid_index+1
    #             return self.searchArray(m[l:r],target)
    #         else:
    #             return True
    #     return False
    
    # def searchMatrix_v3(self, matrix: List[List[int]], target: int) -> bool:
    #     return searchArray_v2(matrix,target)