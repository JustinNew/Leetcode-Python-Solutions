class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 0
        if x < 0:
            x = -1*x
            flag = 1

        result = 0
        while x > 0:
            result = result*10 + x%10
            x = int(x/10)

        if result > 0x7fffffff:
            return 0
        elif flag == 1:
            return -1*result
        else:
            return result
