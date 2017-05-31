class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        else:
            primes = [2,3]
            for i in range(5,n,2):
                flag = 0
                for j in primes:
                    if i%j == 0:
                        flag = 1
                        break
                if flag == 0:
                    primes.append(i)
            return len(primes)

if __name__=='__main__':

    so = Solution()
    print (so.countPrimes(20000))
