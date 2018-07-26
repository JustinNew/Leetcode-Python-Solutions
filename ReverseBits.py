# 190. Reverse Bits

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):


        result = 0
        count = 0
        while n:

            t = n & 1
            result = result * 2 + t
            n = int(n / 2)
            count += 1
            
        for i in range(32 - count):
            result = result * 2

        return result
