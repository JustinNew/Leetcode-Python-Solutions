# 309. Best Time to Buy and Sell Stock with Cooldown

# DP
# For each day, there is three possible actions: buy, sell, cool.
# Build up the table for maxProfit.

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        change = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            change[i] = prices[i] - prices[i - 1]

        buy = [0 for i in range(len(change))]
        sell = [0 for i in range(len(change))]
        cool = [0 for i in range(len(change))]
        for i in range(1, len(change)):
            buy[i] = max(buy[i - 1] + change[i], cool[i - 1])
            sell[i] = buy[i - 1] + change[i]
            cool[i] = max(sell[i - 1], cool[i - 1])

        return max(buy[-1], sell[-1], cool[-1])

if __name__ == '__main__':

    so = Solution()
    print(so.maxProfit([1,2,3,0,2]))
