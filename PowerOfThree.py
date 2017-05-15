class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n>0:
            if n == 1:
                return True
            elif n%3!=0:
                return False
            n = n // 3
            print (n)

if __name__ == '__main__':

    a = 54
    so = Solution()

    print (so.isPowerOfThree(a))
