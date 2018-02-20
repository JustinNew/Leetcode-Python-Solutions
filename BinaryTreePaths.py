# 257. Binary Tree Paths
# Facebook Tag

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        result = []
        temp = []

        if not root:
            return []

        self.util(root, temp, result)

        r = []
        for i in result:
            t = str(i[0])
            for j in range(1,len(i)):
                t = t + '->' + str(i[j])
            r.append(t)

        return r

    def util(self, root, temp, result):

        if not root.left and not root.right:
            result.append(temp+[root.val])
            return

        if root.left:
            self.util(root.left, temp+[root.val], result)

        if root.right:
            self.util(root.right, temp+[root.val], result)

        return
