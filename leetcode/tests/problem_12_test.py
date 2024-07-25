#import inc_dec    # The code to test
import unittest   # The test framework
from codes.problem_12 import Solution


class Test_TestIncrementDecrement(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.s = Solution()


    def test_1(self):        
        self.assertIsInstance(self.s,Solution)
        self.assertEqual(self.s.intToRoman(1), 'I')
        self.assertEqual(self.s.intToRoman(2), 'II')
        self.assertEqual(self.s.intToRoman(3), 'III')
        self.assertEqual(self.s.intToRoman(4), 'IV')
        self.assertEqual(self.s.intToRoman(5), 'V')
        self.assertEqual(self.s.intToRoman(6), 'VI')
        self.assertEqual(self.s.intToRoman(7), 'VII')
        self.assertEqual(self.s.intToRoman(8), 'VIII')
        self.assertEqual(self.s.intToRoman(9), 'IX')
        self.assertEqual(self.s.intToRoman(10), 'X')
        self.assertEqual(self.s.intToRoman(11), 'XI')
        self.assertEqual(self.s.intToRoman(12), 'XII')
        self.assertEqual(self.s.intToRoman(24), 'XXIV')
        self.assertEqual(self.s.intToRoman(39), 'XXXIX')
        self.assertEqual(self.s.intToRoman(39), 'XXXIX')
        self.assertEqual(self.s.intToRoman(48), 'XLVIII')
        self.assertEqual(self.s.intToRoman(85), 'LXXXV')
        self.assertEqual(self.s.intToRoman(95), 'XCV')
        self.assertEqual(self.s.intToRoman(99), 'XCIX')
        self.assertEqual(self.s.intToRoman(322), 'CCCXXII')
        self.assertEqual(self.s.intToRoman(422), 'CDXXII')
        self.assertEqual(self.s.intToRoman(888), 'DCCCLXXXVIII')
        self.assertEqual(self.s.intToRoman(999), 'CMXCIX')
        self.assertEqual(self.s.intToRoman(3000), 'MMM')
    

if __name__ == '__main__':
    unittest.main()