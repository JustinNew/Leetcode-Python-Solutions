# 131. Palindrome Partitioning

# Intuition recursive solution
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
