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

if __name__ == '__main__':

    s = Solution()
    print (s.numDecodings('4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948'))
             
