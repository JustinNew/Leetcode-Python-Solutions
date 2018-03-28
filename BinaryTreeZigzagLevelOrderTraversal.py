# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        s = []
        s.append(root)

        result = []
        flag = 1

        while True:

            temp = []
            ts = []
            for i in s:
                if i.left:
                    ts.append(i.left)
                if i.right:
                    ts.append(i.right)
                temp.append(i.val)

            if flag == -1:
                temp = temp[::-1]

            result.append(temp)
            flag *= -1

            if len(ts) == 0:
                return result
            else:
                s = ts
