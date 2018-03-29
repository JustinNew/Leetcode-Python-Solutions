# 95. Unique Binary Search Trees II

# How to generate enough root node.

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [[]]
        return self.dfs(1, n+1)
        
    def dfs(self, start, end):
        if start == end:
            return None
        result = []
        for i in xrange(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i+1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result
