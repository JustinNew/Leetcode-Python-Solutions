# 191. Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 0
        while n > 0:
            result += n & 1
            n = int(n / 2)

        return result
