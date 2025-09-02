

#САМ НЕ СМОГ РЕШИТЬ
#вариант 1 из решения
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text1))
        longest = 0
        for c in text2:
            cur_length = 0
            for i,val in enumerate(dp):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dp[i] = cur_length + 1
                    longest = max(longest, dp[i])
        return longest

#вариант из подсказок (после просмотра решения)
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [
#             [0] * (len(text2))
#         ] * (len(text1))
#         longest = 0
#         N1 = len(text1)
#         N2 = len(text2)
#         for i in range(N1):
#             for j in range(N2):
#                 _i,_j = max(0,i - 1),max(0, j - 1)
#                 if text1[i] == text2[j]:                    
#                     dp[i][j] = dp[_i][_j] + 1
#                 else:
#                     dp[i][j] = max(dp[_i][j], dp[i][_j])
#         print(dp)