# 129. Sum Root to Leaf Numbers

# 1. Use post-order traversal with additional flag.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        s = []
        result = 0
        if root.left or root.right:
            s.append((root, False, 1))
        else:
            s.append((root, False, 0))

        while True:

            n, visited, haschild = s.pop()
            if visited and not haschild:
                t = ''
                for i in s:
                    t_n, t_v, t_c = i
                    if t_v:
                        t.append(str(t_n.val))
                t.append(str(n.val))
                result += int(''.join(t))
            elif not visited:
                s.append((n, True, haschild))
                if n.right:
                    if n.right.left or n.right.right:
                        s.append((n.right, False, 1))
                    else:
                        s.append((n.right, False, 0)) 
                if n.left:
                    if n.left.left or n.left.right:
                        s.append((n.left, False, 1))
                    else:
                        s.append((n.left, False, 0)) 

            if not s:
                return result   
