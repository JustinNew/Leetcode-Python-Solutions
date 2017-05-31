class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {1:1, 2:1}
        for i in range(3,n+1):
            tMax = 2*(i-2)
            for j in d.keys():
                k = i - j
                temp = max(j*k, d[j]*k, j*d[k])
                if temp > tMax:
                    tMax = temp
            d[i] = tMax
        return d[n]
