# 7. Reverse Integer

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 1
        if x == 0:
            return 0
        elif x < 0:
            flag = -1
            x *= -1

        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = int(x / 10)
            
        result = result * flag
        
        if result > 2 ** 31 - 1 or result < -1 * 2 ** 31:
            return 0
        else:
            return result
