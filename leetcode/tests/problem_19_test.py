#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_19_remove_nth_node_from_end_of_list import Solution


class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()


    def test_1(self):        
        self.assertIsInstance(self.s,Solution)
        #self.assertEqual(self.s, True)

    def test_2(self):
        self.assertIsInstance(self.s,Solution)
        #self.assertEqual(self.s., False)

if __name__ == '__main__':
    unittest.main()