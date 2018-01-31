# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []
        temp = []

        if k > n:
            return []

        if k == n:
            temp = [i+1 for i in range(n)]
            result.append(temp)
            return result

        self.util(0, 0, n, k, temp, result)
  
        return result

    def util(self, i, j, n, k, temp, result):

        if i == k:
            result.append(temp)
            return

        if n - j  >= k - i:
            for l in range(j, n):
                self.util(i+1, l+1, n, k, temp+[l+1], result)

        return

if __name__ == '__main__':

  s = Solution()
  print (s.combine(4,2))
