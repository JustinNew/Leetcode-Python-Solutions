# 139. Word Break

# 1. Recursive Approach: Time Limit Exceeded.

# 2. Think about build a table to reduce repeated calculation
#    The trick is how to create table and store data.

class Solution(object):

    ################################################################################################################
    # Intuition recursive solution
    # Time limit exceeded

    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if s in wordDict:
            return True

        if len(s) == 1 and s not in wordDict:
            return False

        for i in range(1, len(s)):
            if self.wordBreak(s[:i], wordDict) and self.wordBreak(s[i:], wordDict):
                return True

        return False

    ################################################################################################################
    # Dynamic program
    # dp is the answer of your question
    # dp[start][end]
    # For any mid between [start, end], if dp[start][mid] and dp[mid][end] both true, then dp[start][end] is True

    # Build a table to track recursive calculations. 
    # (EndIndex, NumberofString)
    # Build a table to track whether a string ending in EndIndex and have NumberofString can be breaked.
    # Need to find (n, n) 
    # (1, 1): (1, 1) 
    # (2, 2): ((2, 1) and (1, 1)) or (2, 2)
    # (3, 3): ((3, 1) and (2, 2)) or
    #         ((3, 2) and (1, 1)) or
    #         (3, 3)
    # ...
    # (n, n): ((n, 1) and (n - 1, n - 1)) or
    #         ((n, 2) and (n - 2, n - 2)) or
    #         ...
    #         (n, n)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        l = len(s)
        table = [[0 for i in range(l + 1)] for j in range(l + 1)]
        table[0][0] = 1

        for i in range(1, l + 1):
            flag = 0
            for j in range(1, i + 1):
                k = i - j
                if s[(i - j):i] in wordDict:
                    table[i][j] = 1
                if table[i][j] * table[k][k]:
                    flag = 1
            if flag == 1:
                table[i][i] = 1

        if table[l][l]:
            return True
        else:
            return False
