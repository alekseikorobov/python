#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_74_search_a_2d_matrix import Solution
import codes.common as common

class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()

    def test_array(self):
        for array,target,result_ex in [
            ([1,3,5,7], 3, True),
            ([1,3,5,7], 33, False),
            ([1], 1, True),
            ([3], 1, False),
            ([1], 2, False),
            ([1,2], 2, True),
            ([1,2], 1, True),
            ([0,1,2,3,4,5,6,7], 1, True),
            (list(range(0,10)), 1, True),
            (list(range(10,100)), 1, False),
            (list(range(10,100)), 12, True),
            (list(range(10,100)), -12, False),            
            *[
                (list(range(0,1000)), i, True)
                    for i in range(0,1000)                
            ]
        ]:
            result_fact = self.s.searchArray(array,target)
            self.assertEqual(result_fact,result_ex)
    
    def test_matrix(self):
        for matrix,target,result_ex in [
            ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
        ]:            
            result_fact = self.s.searchMatrix(matrix,target)            
            self.assertEqual(result_fact,result_ex)

if __name__ == '__main__':
    unittest.main()