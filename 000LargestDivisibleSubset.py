# 368. Largest Divisible Subset

'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
----------

We first do some math work. For two numbers, A and B, if A < B, A % B must > 0 (A != 0). The only chance A % B == 0 must be A >= B.

With this idea, we sort the list. Then, the question turns similar to no.300 longest increasing subsequence. For ith number, its largest divisible subset is the max of subset of any j from 0 - i-1 in which nums[i] % nums[j] == 0.
'''

# Sort the nums
# If A > B > C and A % B == 0 and B % C == 0, then A % C == 0.
# Dynamic Programming DP[n] = [1, 2, 4, ...]
# Similar to Maximum Subarray

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []
        
        nums.sort()

        dp = [[] for i in range(len(nums))]

        for i in range(len(nums)):

            cur = []
            for j in range(i):
                if len(dp[j]) != 0 and nums[i] % dp[j][-1] == 0 and len(dp[j]) > len(cur):
                    cur = dp[j]
            dp[i] = cur + [nums[i]]

        result = [(dp[i], len(dp[i])) for i in range(len(dp))]
        result.sort(key=lambda x: x[1])

        return result[-1][0]
