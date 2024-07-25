#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_07_palindrome_number import Solution


class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()


    def test_increment(self):        
        self.assertEqual(self.s.isPalindrome(121), True)

    def test_decrement(self):
        self.assertEqual(self.s.isPalindrome(-121), False)

if __name__ == '__main__':
    unittest.main()