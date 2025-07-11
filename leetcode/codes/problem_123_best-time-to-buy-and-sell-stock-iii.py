from types import List

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        for i,p in enumerate(prices):            
            start_index = i
            max_diff = 0
            while start_index < N and max_diff<=prices[start_index] - p:
                max_diff = prices[start_index] - p
                start_index += 1