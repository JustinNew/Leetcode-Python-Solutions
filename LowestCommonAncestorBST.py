# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        a1 = self.Ancestors(root, p)
        a2 = self.Ancestors(root, q)

        result = None
        for i in range(min(len(a1),len(a2))):
            if a1[i] == a2[i]:
                result = a1[i]

        return result

    def Ancestors(self, root, x):

        nodes = []

        while True:
            nodes.append(root)
            if root:
                if x.val > root.val:
                    root = root.right
                elif x.val < root.val:
                    root = root.left
                else:
                    return nodes
            else:
                return None
                

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
