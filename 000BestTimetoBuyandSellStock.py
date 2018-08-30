# 121. Best Time to Buy and Sell Stock

# DP
# 1. Track the lowest price so far L[i]
# 2. Max profit so far P[i] 
# 3. P[i] = max(P[i - 1], price[i] - L[i])

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        low = prices[0]
        m = 0
        for i in range(1,len(prices)):
            m = max(m, prices[i] - low)
            if prices[i] < low:
                low = prices[i]
                
        return m
