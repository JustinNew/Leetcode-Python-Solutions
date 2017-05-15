class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1:
            return 1

        return self.climbStairs(n-1)+self.climbStairs(n-2)
