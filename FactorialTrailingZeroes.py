# 172. Factorial Trailing Zeroes

# Can "5" in numbers. 

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = 0
        while int(n / 5) > 0:
            res += int(n / 5)
            n = int(n / 5)
        
        return res
