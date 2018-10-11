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

    def reverseBits(self, n):
        
        res = []
        while n > 0:
            t = n % 2
            res.append(t)
            n = int(n / 2)
            
        l = len(res)
        if l < 32:
            for i in range(32 - l):
                res.append(0)
                
        s = 0
        res.reverse()
        for i in range(32):
            s += res[i] * 2 ** i
            
        return s
