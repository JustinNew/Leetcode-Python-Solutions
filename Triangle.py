# 120. Triangle

# DP
# Memory use O(n)

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        n = len(triangle)

        result = [0 for i in range(n)]

        for i in range(1, n + 1):
            temp = [result[k] for k in range(len(result))]

            for j in range(i):
                if j == 0:
                    result[j] = temp[j] + triangle[i - 1][j]   
                elif j == i - 1:
                    result[j] = temp[j - 1] + triangle[i - 1][j]
                else:
                    result[j] = min(temp[j] + triangle[i - 1][j], temp[j - 1] + triangle[i - 1][j])  
           
        return min(result)
