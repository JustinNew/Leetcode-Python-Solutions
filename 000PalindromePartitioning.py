# 131. Palindrome Partitioning

# 1. Recursion solution
# Some similarity to 95. Unique Binary Search Trees II

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if len(s) == 0:
            return [[]]

        if len(s) == 1:
            return [[s]]

        result = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for l in self.partition(s[i:]):
                    result.append([s[:i]] + l)

        return result

'''
2. Dynamic Programming
   dp[n] = dp[n - 1] + [s[n]] 
         + dp[n - 2] + [s[n - 1, n]] if s[n - 1, n] is palindrome
         + dp[n - 3] + [s[n - 2, n - 1, n]] if s[n - 2, n - 1, n] is palindrome 
         ...
         + dp[1] + [s[1:]] if s[1:] is palindrome
'''

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if len(s) == 0:
            return []

        dp = [[] for i in range(len(s))]
        dp[0] = [[s[0]]]

        for i in range(1, len(s)):
            for j in range(i):
                t = s[i - j:i + 1]
                if t == t[::-1]:
                    for l in dp[i - j - 1]: 
                        dp[i].append(l + [t])
            t = s[:i + 1]
            if t == t[::-1]:
                dp[i].append([t]) 

        return dp[-1]       
