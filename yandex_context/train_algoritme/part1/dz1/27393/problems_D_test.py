

import unittest

import problems_D

class MyTest(unittest.TestCase):
    def test_solve(self):
      # result = problems_D.solve(1,0,0)
      # self.assertEqual(result, 0)

      # result = problems_D.solve(1,2,3)
      # self.assertEqual(result, 7)

      # result = problems_D.solve(1,2,-3)
      # self.assertEqual(result, problems_D.NO_SOLUTION)


      # result = problems_D.solve(3,-1,1)
      # self.assertEqual(result, problems_D.NO_SOLUTION)

      case_list = [
        (-1,-1,-1,problems_D.NO_SOLUTION),

        (0, 0, 0, problems_D.MANY_SOLUTIONS),

        (0, 4, 2, problems_D.MANY_SOLUTIONS),
        (0, 4, 3, problems_D.NO_SOLUTION),

        (0, 1, 0, problems_D.NO_SOLUTION),
        (0,-1, 0, problems_D.NO_SOLUTION),
        
        (-1, 0, 0, 0),
        ( 1, 0, 0, 0),

        (-1, 1, 0, 1),
        ( 1, 1, 0,-1),
        ( 1, 1, 1,0),
        (2, 4, 0, int(-4/2)),
        (2, 5, 0,problems_D.NO_SOLUTION),

        (-1,-1, 1,-2),

        (-1,0, 1,-1),

        (-1,1, 1,0),


        (1,1, 1,0),

        (0,0,1,problems_D.NO_SOLUTION),
        (0,1,1,problems_D.MANY_SOLUTIONS),
        (0,3,2,problems_D.NO_SOLUTION),
        
        (1,0,2,4),

      ]
      for a,b,c,res in case_list:
        result_fact = problems_D.solve(a,b,c)
        self.assertEqual(res,result_fact,f'{a=},{b=},{c=},{res=},{result_fact=}')


if __name__ == "__main__":
  unittest.main()