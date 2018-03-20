# 44. Wildcard Matching

# 1.
# Recursion.
# The key is how to match '*'.

# 2.
# Using recursion, there is a lot of repeated computation.
# So, build up a table.
# Very careful when building the table.
# Make clear logic first.

# 3.
# DP
# It's actually the same as two by simplify the table to an array.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) == 0:
            if p[0] == '*':
                return self.isMatch(s, p[1:])
            else:
                return False
        elif len(p) == 0:
                return False

        if p[0] == '*':
            flag = 0
            for i in range(len(s) + 1):
                if self.isMatch(s[i:], p[1:]):
                    flag = 1
            if flag == 1:
                return True
            else:
                return False
        else:
            if p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            elif s[0] == p[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return False


    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        m = len(p)
        n = len(s)

        if len(p) - p.count('*') > n:
            return False

        if m == 0 and n == 0:
            return True
        elif m == 0:
            return False
        elif n == 0:
            if set(p) != set('*'):
                return False
            else:
                return True

        # '*' matches '', so need to have n + 1 columns.
        match = [[False for j in range(n + 1)] for i in range(m)]

        if p[0] == '*':
            for i in range(n + 1):
                match[0][i] = True
        elif p[0] == '?':
            match[0][1] = True
        elif p[0] == s[1]:
            match[0][1] = True
        
        for i in range(1, m):
            if p[i] == '*':
                for j in range(0, n + 1):
                    flag = 0
                    for k in range(j, -1, -1):
                        if match[i - 1][k]:
                            flag = 1
                    if flag == 1:
                        match[i][j] = True
            elif p[i] == '?':
                for j in range(1, n + 1):
                    if match[i - 1][j - 1] == True:
                        match[i][j] = True
            else:
                for j in range(1, n + 1):
                    if p[i] == s[j - 1] and match[i - 1][j - 1]:
                        match[i][j] = True 

        return match[m - 1][n]

    def isMatch3(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

if __name__ == '__main__':

    s = Solution()
    if s.isMatch2("abbaabbababbbbaaabbaabaabbbabbbbaaaaabababbbabbaabababbbabbbaababbabaaaabbabababaaabbbaaaabaaaabbaaaababaabbabaababbbabaaaaabbaabaaabbbababbbbabbbaabbabbbaaaabbabbaabaabbbbababbababaaababbaaaabaaabaaabb", "b**baabaa****ba*a**ab*abb*a*abbbba*baaba****a*aa**b*bba*ba*b*****ba***abb******ab***bab*aa***bb****b"):
        print('Matched.')
    else:
        print('Did not match.')
