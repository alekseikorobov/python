#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_10 import Solution


class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()

    def test_1(self):        
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.isMatch("a",".") , True)

    def test_2(self):        
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.isMatch("aa","..") , True)

    def test_3(self):        
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.isMatch("aa",".") , False)

    def test_4(self):
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.isMatch("ab",".bс") , False)

    def test_5(self):
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.isMatch("aa","a") , False)

    def test_6(self):
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.isMatch("aa","a*") , True)

    def test_7(self):
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.isMatch("ab",".*") , True)

if __name__ == '__main__':
    unittest.main()