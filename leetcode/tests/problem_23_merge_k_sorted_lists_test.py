#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_23_merge_k_sorted_lists import Solution
import codes.common as common

class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()

    def test_2(self):
        for list,result_e in [
            ([[1,4,5],[2,6]]   , [1,2,4,5,6]),
            ([[1,4,5],[1,3,4]], [1,1,3,4,4,5]),
            ([[1,4,5],[1,3,4],[2,6]] , [1,1,2,3,4,4,5,6]),
            ([],[]),
            ([[]],[]),
        ]:
            list_n = [common.build_nodes(l) for l in list]
            
            result_n = self.s.mergeKLists(list_n)
            result_l = common.toArray(result_n)
            self.assertEqual(result_l,result_e)

if __name__ == '__main__':
    unittest.main()