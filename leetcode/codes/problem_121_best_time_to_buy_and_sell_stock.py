class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = prices[0]
        max_v = float('-inf')
        max_diff = 0        
        for i in range(1,len(prices)):
            p = prices[i]
            if p > max_v and p > min_v:
                max_v = p
                diff = max_v - min_v
                if diff > max_diff:
                    max_diff = diff
            elif p < min_v:
                min_v = p
                max_v = p
        return max_diff
    
#O(N)

#решение из ответов
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit