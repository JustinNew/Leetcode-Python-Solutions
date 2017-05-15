# Find the maximum depthn of a tree.

class Solution:

    def maxDepth(self, root):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
