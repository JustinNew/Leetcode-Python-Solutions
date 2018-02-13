# 634. Find the Derangement of An Array
# Dynamics programming: d(n)=(n−1)∗[d(n−1)+d(n−2)]

class Solution:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
 
        # Whenever there is one more derangement, add '1' in to result.
        result = []
        flag =[0 for i in range(n)]

        self.util(0, n, flag, result)

        if sum(result) > pow(10, 9):
            return sum(result) % pow(10, 9) + 7
        else:
            return sum(result)

    def util(self, pos, n, flag, result):

        if pos == n:
            return result.append(1)

        for i in range(n):
            if i != pos and flag[i] != 1:
                flag[i] = 1
                self.util(pos+1, n, flag, result)
                flag[i] = 0

        return

class Solution2:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        mul = 1
        sum = 0
        M = 1000000007

        for i in range(n, -1, -1):
            if i % 2 == 0:
                temp = 1
            else: 
                temp = -1
            sum = (sum + M + mul * temp) % M
            mul = (mul * i) % M

        return sum 

if __name__ == '__main__':

    s = Solution()
    print (s.findDerangement(10))
