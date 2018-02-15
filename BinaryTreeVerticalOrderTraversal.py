# 314. Binary Tree Vertical Order Traversal
# Facebook Tag
# Do level order travesal and trick is associating column.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # Inorder Travesal and give associated column number.
        # Root 0, left -1 and right +1.

        if not root:
            return []

        result = []

        self.util2(root, 0, result)

        # Order the result list in to List of Lists.
        result.sort(key=lambda x: x[1])

        ll = []
        t_c_o = float('-inf')
        temp = []
        for i in range(len(result)):
            (value, c) = result[i]
            if c != t_c_o:
                if len(temp) != 0:
                    ll.append(temp)
                    temp = []
                t_c_o = c

            temp.append(value)

        ll.append(temp)
                
        return ll

    # This Inorder Traveral does not pass Leetcode.
    def util(self, root, column, result):

        result.append((root.val, column))

        if root.left:
            util(root.left, column - 1, result)

        if root.right:
            util(root.right, column + 1, result)

        return

    # Use Level Order Travesal.
    def util2(self, root, column, result):

        nodes = []
        nodes.append((root, column))

        while True:

            temp = []
            for i in range(len(nodes)):
                (t, c) = nodes[i]
                result.append((t.val, c))

                if t.left:
                    temp.append((t.left, c - 1))
                if t.right:
                    temp.append((t.right, c + 1))

            if len(temp) == 0:
                return
            else:
                nodes = temp
