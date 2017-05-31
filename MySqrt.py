class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        a = 1.0
        b = x

        while abs(a-b)>1:
            a = (a+b)/2
            b = x/a
            print (a,b)

        return int((a+b)/2)

so = Solution()
print (so.mySqrt(5000))
