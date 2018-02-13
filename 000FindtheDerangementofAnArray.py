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
        
        result = [0 for i in range(n+1)]
        result[0] = 0
        result[1] = 0
        result[2] = 1
        for i in range(3, n+1):
            result[i] = (i-1)*(result[i-1] + result[i-2])
            
        return result[-1] 

if __name__ == '__main__':

    s = Solution2()
    print (s.findDerangement(10))
