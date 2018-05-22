# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Time Limit Exceeded. 
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        s = []
        s.append(root)
        result = 0

        while True:

            temp = []
            for i in s:
                result += 1
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)

            if len(temp) == 0:
                return result

            s = temp

    # 1. DFS to get the depth of the tree
    # 2. Right-first-inorder traveral to find not complete nodes
    # 3. Calculate the total number of 

    # Time Limit Exceeded.
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        level = 0
        n = root
        while n.left:
            n = n.left
            level += 1

        total = 0
        for i in range(level + 1):
            total += 2 ** i

        s = []
        s.append((root, False, 0))

        missed = 0
        while len(s) != 0:
            n, flag, t_level = s.pop()
            if flag:
                if t_level == level:
                    return total - missed
                if not n.right:
                    for i in range(level - t_level):
                        missed += 2 ** i
                if not n.left:
                    for i in range(level - t_level):
                        missed += 2 ** i
            else:
                if n.left:
                    s.append((n.left, False, t_level + 1))
                s.append((n, True, t_level))
                if n.right:
                    s.append((n.right, False, t_level + 1))

        return total - missed
