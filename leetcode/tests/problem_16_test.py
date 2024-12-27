#import inc_dec    # The code to test
import unittest  # The test framework

from codes.problem_16_3sum_closest_2 import Solution


class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()


    def test_1(self):        
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.threeSumClosest([-1,2,1,-4],1), 2)

    def test_2(self):
        self.assertIsInstance(self.s,Solution)
        #self.assertEqual(self.s., False)

if __name__ == '__main__':
    unittest.main()