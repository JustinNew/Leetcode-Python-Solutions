# 91. Decode Ways
# Facebook Tag

class Solution:
    def numDecodings(self, s):

            # dp[i] = dp[i-1] if s[i] != "0"
            #       + dp[i-2] if "09" < s[i-1:i+1] < "27"

            if s == "": return 0

            dp = [0 for x in range(len(s)+1)]
            dp[0] = 1

            for i in range(1, len(s)+1):
                if s[i-1] != "0":
                    dp[i] += dp[i-1]

                if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  # "01"ways = 0
                    dp[i] += dp[i-2]

            return dp[len(s)]

'''
Dynamic Programming
if s[i] != 0:
    dp[i] += dp[i - 1]

if s[i - 2:i] >= 10 and s[i - 2:i] <= 26:
    dp[i] += dp[i - 2]
'''
    ########################################################################################################################
    # My solution.

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        if s[0] == '0' or l == 0:
            return 0
        elif l == 1:
            return 1

        dp = [0 for i in range(l)]
        
        dp[0] = 1
        if s[1] == '0':
            if s[0] <= '2':
                dp[1] = 1
            else:
                return 0
        else:
            if s[:2] >= '10' and s[:2] <= '26':
                dp[1] = 2
            else:
                dp[1] = 1
        
        for i in range(2, l):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1:i + 1] >= '10' and s[i - 1:i + 1] <= '26':
                dp[i] += dp[i - 2]

        return dp[-1]
