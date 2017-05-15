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
