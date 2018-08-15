# 96. Unique Binary Search Trees

# Suppose you are given 1,..., n, and you want to generate all binary search trees. 
# How do you do it? Suppose you put number i on the root, then simply
# 1. Generate all BST on the left branch by running the same algorithm with 1–(i-1),
# 2. Generate all BST on the right branch by running the same algorithm with (i+1)–n.
# 3. Take all combinations of left branch and right branch, and that’s it for i on the root.

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]   
