# 298. Binary Tree Longest Consecutive Sequence
# Google Tag

# Go through every node and then do a DFS search.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Time Limit Exceeded. 
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       
        if not root:
            return 0

        s = []
        s.append(root)
        m = 1

        # Do a level travesal.
        while True: 

            temp = []
            for i in s:
                t = self.util(i)
                if t > m:
                    m = t

                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)

            if len(temp) == 0:
                return m

            s = temp

    def util(self, root):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if root.left and root.left.val == root.val + 1:
            return 1 + self.util(root.left)

        if root.right and root.right.val == root.val + 1:
            return 1 + self.util(root.right)

        return 1

    # DFS and Pass down information.
    def longestConsecutive2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        m = 1

        if not root:
            return 0

        m = self.util2(root, None, 0, m)

        return m

    def util2(self, root, p, length, m):

        if p and root.val == p.val + 1:
            length += 1
        else:
            length = 1
        m = max(m, length)
   
        if root.left:
            m = self.util2(root.left, root, length, m)

        if root.right:
            m = self.util2(root.right, root, length, m)

        return m      
