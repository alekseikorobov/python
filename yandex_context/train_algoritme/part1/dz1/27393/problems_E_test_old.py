

import unittest

import problems_E

class MyTest(unittest.TestCase):
    def test_solve(self):

      case_list = [
        ('89 20 41 1 11','2 3'),
        ('11 1 1 1 1','0 1'),
        ('3 2 2 2 1','0 1'),
      ]
      for data_input,data_output in case_list:
        K1, M, K2, P2, N2 = map(int,data_input.split())
        P1_ex, N1_ex = map(int,data_output.split())
        P1_fact, N1_fact  = problems_E.solve(K1, M, K2, P2, N2)
        
        self.assertEqual(P1_ex,P1_fact,f'{data_input=}; {data_output=}. {P1_fact=}, {N1_fact=}')
        self.assertEqual(N1_ex,N1_fact,f'{data_input=}; {data_output=}. {P1_fact=}, {N1_fact=}')


if __name__ == "__main__":
  unittest.main()