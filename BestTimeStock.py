# 122. Best Time to Buy and Sell Stock II

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        buy = prices[0]
        sell = prices[0]

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                sell = prices[i]
            else:
                profit += sell - buy
                buy = prices[i]
                sell = prices[i]

        profit += sell - buy
        return profit

    # Get daily difference.
    # Maximum profit is the sum of all positive.
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        diff = []
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i - 1])
            
        res = 0
        for num in diff:
            if num > 0:
                res += num
                
        return res
