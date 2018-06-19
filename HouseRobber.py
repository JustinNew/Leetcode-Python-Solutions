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


# From Online
'''
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
'''

    def robUnoptimized(self, xs):
        '''Robbing a house in O(n) time and O(n) space.'''
        if not xs:
            return 0
        n = len(xs)
        dp = [0 for _ in range(n)]
        for j in range(n):
            cont = xs[j]
            if j >= 2:
                cont += dp[j-2]
            stop = dp[j-1] if j >= 1 else 0
            dp[j] = max(cont, stop)
        return dp[-1]

    def rob(self, xs):
        '''Robbing a house in O(n) time and O(1) space.'''
        res = 0
        if not xs:
            return res
        a, b = 0, 0
        for x in xs:
            res = max(a+x, b)
            a, b = b, res
        return res
