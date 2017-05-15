class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        times = 100
        while times > 0:
            if n==1:
                 return True

            sum = 0
            while n > 0:
                temp = n%10
                n = n // 10
                sum += temp*temp

            n = sum
            times -= 1

        if times == 0:
            return False

if __name__=='__main__':

     a = 68
     so = Solution()
     print(so.isHappy(a))
