
# по сути это решение того же фибоначи.
# дело в том, что добавление новой ступеньки, это означает,
# что к предыдущему варианту можно прибавить к каждому значение 1,
# а к пред-предыдущему варианту добавить 2, тогда количество вариантов возврастает на N-2 + N-1

# вариант без мемоизации (за время O(2^N)) не умещается по тестам: 
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0: return 0
#         if n == 1: return 1
#         if n == 2: return 2
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# так за время O(N) работает корректно:
class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memo: return self.memo[n]
        if n < 3: return n 
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]