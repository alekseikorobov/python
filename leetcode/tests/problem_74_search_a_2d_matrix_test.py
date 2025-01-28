#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_34_find_first_and_last_position_of_element_in_sorted_array import Solution
import codes.common as common

class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()

    def test_array(self):
        for array,target,result_ex in [
            ([5,7,7,8,8,10], 8, [3,4]),
            ([5,7,7,8,8,10], 6, [-1,-1]),
            ([], 0, [-1,-1]),
            ([2,2], 2, [0,1]),
            ([1,1,2],1,[0,1])
        ]:
            result_fact = self.s.searchRange(array,target)
            self.assertEqual(result_fact,result_ex)
    
    def _test_search(self):
        for a,target,result_ex in [
            ([1,3,5,7], 3, (True,1)),
            ([1], 3, (False,-1)),
            ([3], 1, (False,-1)),
            ([1,2], 1, (True,0)),
            ([1,2], 2, (True,1)),
            ([1,2,3], 3, (True,2)),
            ([1,2,3], 2, (True,1)),
            ([1,2,3], 0, (False,-1)),
            ([1,2,3], 4, (False,-1)),
            ([2,2], 2, (True,0)),
        ]:
            print(f'-'*10)
            result_fact = self.s.search(a,target,0,len(a))
            self.assertEqual(result_fact,result_ex)

if __name__ == '__main__':
    unittest.main()