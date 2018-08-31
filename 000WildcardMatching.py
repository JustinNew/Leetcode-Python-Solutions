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

#     0  a  a  b
# a   N  Y  N  N
# *   N  Y  Y  Y
# a   N  N  Y  N
# *   N  N  Y  N
# b   N  N  N  Y

class Solution:

    ##############################################################################################################
    # Intuition recursive solution
    # Time limit exceeded
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Base Cases
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(p) == 0:
            return False
        elif len(s) == 0:
            if set(p) != set('*'):
                return False
            else:
                return True

        # Recursive matches
        if p[0] != '?' and p[0] != '*':
            if p[0] != s[0]:
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        elif p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        else:
            for i in range(len(s) + 1):
                if self.isMatch(s[i:], p[1:]):
                    return True

            return False

    ##############################################################################################################
    # Recursive solution has a lot of repeated calculation
    # So Dynamic Programming
    # 2-D DP
    # Time Limit Exceeded

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Base case
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(p) == 0:
            return False
        elif len(s) == 0:
            if set(p) != set('*'):
                return False
            else:
                return True
            
        # Row
        n = len(p)
        # Column
        m = len(s)

        # Need to add one column and one row.
        # Initialization if error prone and tricky.
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[i][0] = 1
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] != '?' and p[i - 1] != '*':
                    if p[i - 1] == s[j - 1] and dp[i - 1][j - 1] == 1:
                        dp[i][j] = 1
                        
                elif p[i - 1] == '?':
                    if dp[i - 1][j - 1] == 1:
                        dp[i][j] = 1
                        
                elif p[i - 1] == '*':
                    # '*' can match 0 letter, so it's from 0 to j instead of j - 1.
                    for k in range(j + 1):
                        if dp[i - 1][k] == 1:
                            dp[i][j] = 1  
                            break
                            
        return True if dp[-1][-1] == 1 else False

    ##############################################################################################################
    # Optimize the previous 2-D DP approach.

    def isMatch3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(p) == 0:
            return False
        elif len(s) == 0:
            if set(p) != set('*'):
                return False
            else:
                return True
            
        # Row
        n = len(p)
        # Column
        m = len(s)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        # Need to add one column and one row.
        # Initialization if error prone and tricky.
        dp[0][0] = 1
        for i in range(1, n):
            if p[i - 1] == '*':
                dp[i][0] = 1
            else:
                break

        for i in range(1, n + 1):

            if p[i - 1] != '?' and p[i - 1] != '*':
                for j in range(1, m + 1):
                    if p[i - 1] == s[j - 1] and dp[i - 1][j - 1] == 1:
                        dp[i][j] = 1

            elif p[i - 1] == '?':
                for j in range(1, m + 1):
                    if dp[i - 1][j - 1] == 1:
                        dp[i][j] = 1

            elif p[i - 1] == '*':
                flag = 0
                for j in range(0, m + 1):
                    if dp[i - 1][j] == 1:
                        flag = 1 
                        break
                if flag == 1:
                    for k in range(j, m + 1):
                        dp[i][k] = 1

        return True if dp[-1][-1] == 1 else False
