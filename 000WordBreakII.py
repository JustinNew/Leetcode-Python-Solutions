# 140. Word Break II

class Solution(object):

    # Time Limit Exceeded.
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        if len(s) == 0 or len(wordDict) == 0:
            return []

        result = []
        def util(i, list):
            if i == len(s):
                result.append(' '.join(list))
                return 

            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    util(j + 1, list + [s[i:j + 1]])

            return 

        util(0, [])
        return result


    # Dynamic programming
    # Build a table to record the possible words
    # dp[start][end]
    # Memory Limit Exceeded

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0 or len(wordDict) == 0:
            return []

        n = len(s)
        dp = [[[] for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(i, -1, -1):
                if s[j:i + 1] in wordDict:
                    dp[j][i] = [s[j:i + 1]] 
            for j in range(i - 1, -1, -1):
                if dp[0][j] and dp[j + 1][i]:
                    for w1 in dp[0][j]:
                        for w2 in dp[j + 1][i]:
                            dp[0][i] += [w1 + ' ' + w2]

        return dp[0][n - 1]              

    # Dynamic programming
    # Further simplify
    # The forward DP solution will cause MLE while the backward DP is just fine

    def wordBreak3(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0 or len(wordDict) == 0:
            return []

        n = len(s)
        dp = [[] for i in range(n)]
                
        for i in range(n):
            if s[0:i + 1] in wordDict:
                dp[i] = [s[0:i + 1]]
                
            for j in range(i - 1, -1, -1):  
                if s[j + 1:i + 1] in wordDict and dp[j]:
                    for w1 in dp[j]:
                        dp[i] += [w1 + ' ' + s[j + 1:i + 1]] 
               
        return dp[n - 1] 

    # From Discussion
    # Backward DP

    def wordBreak4(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                       for j in range(i+1, len(s)+1)
                       if s[i:j] in wordDict
                       for tail in sentences(j)]
            return memo[i]
        return sentences(0)
