# 543. Diameter of Binary Tree
# Facebook Tag

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        if not root.left and not root.right:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)

        d = l + r

        d_l = self.diameterOfBinaryTree(root.left)
        d_r = self.diameterOfBinaryTree(root.right)

        t = max(d_l, d_r)
        
        return max(d, t)            

    def depth(self, root):

        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return 1 + self.depth(root.right)
        elif not root.right:
            return 1 + self.depth(root.left)
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1

    # Improve by build up a table to depth.
    # Level travesal to get max diameter.
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        d = {None: 0}
        
        def depth(root):
            if root in d:
                return
            else:
                depth(root.left)
                depth(root.right)
                d[root] = max(d[root.left], d[root.right]) + 1
                
            return 
        
        depth(root)
        m = d[root.left] + d[root.right]
        l = [root]
        while True:
            temp = []
            for i in l:
                if d[i.left] + d[i.right] > m:
                    m = d[i.left] + d[i.right]
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if len(temp) == 0:
                return m
            
            l = temp

    # The above one can be improved.

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        d = {None: 0}

        self.m = 0
        def depth(root):
            if root in d:
                return
            else:
                depth(root.left)
                depth(root.right)
                if d[root.left] + d[root.right] > self.m:
                    self.m = d[root.left] + d[root.right]
                d[root] = max(d[root.left], d[root.right]) + 1

            return

        depth(root)
        return self.m
