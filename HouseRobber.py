# 198. House Robber

class Solution:

    # TLE
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        f1 = nums[0] + self.rob(nums[2:])
        f2 = nums[1] + self.rob(nums[3:])

        return max(f1, f2)

    # The above one have a lot of repeated calculations.
    # Then build a table to memorize the repeated calucations.

    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        rob = [i for i in nums]
        rob[1] = max(nums[:2])

        for i in range(2, len(nums)):
            rob[i] = nums[i] + max(rob[:i - 1])

        return max(rob[-1] , rob[-2])



'''
"determine the maximum amount of money you can rob" -> Max -> Dynamic Programming

dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])
'''

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)

        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums)

        dp = [0 for i in range(l)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, l):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
