



class Solution:

    def get_two(self,ones):
        N = len(ones)
        max_sum = 2
        current = 0
        left_array = []
        start_index = 0
        end_index = 0
        for i in range(0,N):
            a = ones[i] #1
            current = a #1
            start_index = i #0
            while a == 1 and current != max_sum: #true false
                current += 1 #2
                i += 1 #1
                end_index = i #1
                a = ones[i] #1
            yield ones[start_index:]
                




    def climbStairs(self, n: int) -> int:
        
        ones = [1 for _ in range(n)]
        print(f'{ones=}')
        res = self.get_two(ones)
        for r in res:
            print(f'{r=}')


        pass


s = Solution()


print(s.climbStairs(2))