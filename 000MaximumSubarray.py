# 53. Maximum Subarray

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

##############################################################################################################
# Dynamic programming
# If the previous sum so far is negative, then start from itself.
# dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# dp =   [-1, 1, -2, 4,  3, 5, 6,  1, 5]

# Optimized: 
#    1. dp[i] -> curSum, we only need dp[i - 1] for dp[i].
#    2. Use ans to reduce find the maximum of dp list. 

class Solution(object):
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = ans = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            if curSum > ans:
                ans = curSum

        return maxSum
