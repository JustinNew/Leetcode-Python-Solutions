# 338. Counting Bits

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        if num == 0:
            return [0]

        candidate = []
        i = 1
        while i <= num:
            candidate.append(i)
            i *= 2

        result = []
        for i in range(num + 1):
            count = 0
            for j in candidate[::-1]:
                if i >= j:
                    count += 1
                    i -= j
                if i == 0:
                    break
            result.append(count)

        return result
        

    # Dynamic Programming
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        if num == 0:
            return [0]

        dp = [0 for i in range(num + 1)]
        cur, prev = 1, 1
        for i in range(1, num + 1):
            if i == cur:
                dp[i] = 1
                prev = cur
                cur *= 2
            else:
                dp[i] = 1 + dp[i - prev]
        
        return dp 
