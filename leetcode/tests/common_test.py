

import unittest
import codes.common as common

class TestCommon(unittest.TestCase):
    def test_sum_arithmetic_progression_formula(self):
        list = [0, 1, 2, 3]
        sum_result = common.sum_arithmetic_progression_formula(0,1,len(list))
        sum_except = sum(list)
        assert sum_result == sum_except,f"{sum_result=} != {sum_except=}"
        