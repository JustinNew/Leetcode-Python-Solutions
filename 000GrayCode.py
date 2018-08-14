# 89. Gray Code

# Good analysis is needed.
# First for 1 bit
#  0
#  1
# Then for 2 bit, the first two numbers are actually
# 00
# 01
# Flip the 1 bit numbers and add 1 on the second bit
# 00     00
# 01  -> 01
# 01  -> 11
# 00     10
# Then for 3 bit, flip the already have numbers and add 1 in the third bit
# 000     000
# 001     001
# 011     011
# 010  -> 010
# 010  -> 110
# 011     111
# 001     101
# 000     100

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        result = [0, 1]
        for i in range(1, n):
            result += [j + 2 ** i for j in result[::-1]]

        return result
