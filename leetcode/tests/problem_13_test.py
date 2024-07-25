#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_13 import Solution


class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()


    def test_1(self):        
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.romanToInt('I'),1)
        self.assertEqual(self.s.romanToInt('II'),2)
        self.assertEqual(self.s.romanToInt('III'),3)
        self.assertEqual(self.s.romanToInt('IV'),4)
        self.assertEqual(self.s.romanToInt('V'),5)
        self.assertEqual(self.s.romanToInt('VI'),6)
        self.assertEqual(self.s.romanToInt('VII'),7)
        self.assertEqual(self.s.romanToInt('VIII'),8)
        self.assertEqual(self.s.romanToInt('IX'),9)
        self.assertEqual(self.s.romanToInt('X'),10)
        self.assertEqual(self.s.romanToInt('XI'),11)
        self.assertEqual(self.s.romanToInt('XII'),12)
        self.assertEqual(self.s.romanToInt('XXIV'),24)
        self.assertEqual(self.s.romanToInt('XXXIX'),39)
        self.assertEqual(self.s.romanToInt('XXXIX'),39)
        self.assertEqual(self.s.romanToInt('XLVIII'),48)
        self.assertEqual(self.s.romanToInt('LXXXV'),85)
        self.assertEqual(self.s.romanToInt('XCV'),95)
        self.assertEqual(self.s.romanToInt('XCIX'),99)
        self.assertEqual(self.s.romanToInt('CCCXXII'),322)
        self.assertEqual(self.s.romanToInt('CDXXII'),422)
        self.assertEqual(self.s.romanToInt('DCCCLXXXVIII'),888)
        self.assertEqual(self.s.romanToInt('CMXCIX'),999)
        self.assertEqual(self.s.romanToInt('MMM'),3000)

if __name__ == '__main__':
    unittest.main()