
# разобрать решение с помощью задачи - 1143_longest-common-subsequence.py

# Решение: с помощью динамического программирования через рекурсию - 
# https://leetcode.com/problems/jump-game-ii/solutions/2819171/recursive-dp-approach-with-python/

from typing import List


class Solution:

    def __init__(self,is_log = False) -> None:
        self.is_log = is_log

    def log(self, str:str):
        if self.is_log:
            print(str)


    def get_max_index(self, array,start_index, length):
        index = 0
        N = len(array[start_index:])
        part_array = array[start_index:start_index+length]
        m = float('inf')
        self.log(f'\t{array = }, {part_array = } {start_index = } {start_index+length = }')
        min_val = start_index + m
        for i, a in enumerate(part_array):
            if a == 0: continue

            new_var = i + start_index + a

            if min_val >= N - new_var:
                min_val = N - new_var
                m = a
                index = i

        return index + start_index, m

    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1: return 0

        j = 1
        start_index = 0
        length = nums[start_index]
        
        if length >= len(nums):
            return 1

        max_index = 0
        sum_fact = 0

        while start_index + 1 + length < len(nums):
            max_index, value = self.get_max_index(nums, start_index + 1, length)
            start_index = max_index
            length = value
            sum_fact += max_index
            self.log(f'"{start_index = }" "{max_index = }" "{value=}" "{start_index + 1 + length = }" {len(nums)=}')
            j += 1
        self.log(f'{j = }')
        return j


s = Solution(False)
#s = Solution(True)


print(f'{s.jump([0]) == 0 = }')
print(f'{s.jump([9,1,2,3,4,5]) == 1 = }')
print(f'{s.jump([1]) == 0 = }')
print(f'{s.jump([1,1]) == 1 = }')
print(f'{s.jump([1,2,1]) == 2 = }')
print(f'{s.jump([2,1,1]) == 1 = }')
print(f'{s.jump([2,1,1,1]) == 2 = }')
print(f'{s.jump([2,3,1,1,4]) == 2 = }')
print(f'{s.jump([1,2,3,2,4,3,2,1,2]) == 4 = }')
print(f'{s.jump([1,1,1,1]) == 3 = }')
print(f'{s.jump([1,1,1,1,1]) == 4 = }')
print(f'{s.jump([1,1,1,1,1,1]) == 5 = }')
print(f'{s.jump([4,1,1,3,1,1,1]) == 2 = }')
print(f'{s.jump([10,9,8,7,6,5,4,3,2,1,1,0]) == 2 = }')
print(f'{s.jump([1,2,1,1,1]) == 3 = }')
print(f'{s.jump([2,0,2,4,6,0,0,3]) == 3 = }')

