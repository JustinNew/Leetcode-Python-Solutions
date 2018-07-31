# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Recursive
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            if root.left and root.left.left == None and root.left.right == None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:        
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    # Depth First Using Stack
    def sumOfLeftLeaves1(self,root):

        if not root:
            return 0

        s = [root] # list can be directly used as stack.
        res = 0

        while s:
            tmp = s.pop()
            if temp.right:
                s.append(temp.right)
            if tmp.left:
                s.append(temp.left)
                if not temp.left.left and not temp.left.right:
                    res = res + temp.left.val

        return res

    # BFS Using Queue
    def sumOfLeftLeaves2(self, root):

        from collections import deque
        if not root:
            return 0

        s = deque()
        s.append(root)
        res = 0

        while s:
            tmp = s.popleft()
            if tmp.left:
                s.append(tmp.left)
                if not tmp.left.left and not tmp.left.right:
                    res = res + tmp.left.val
            if tmp.right:
                s.append(tmp.right)

        return res

    # Level First Search
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        result = 0
        s = [root]

        while 1:

            temp = []
            for n in s:
                if n.left:
                    temp.append(n.left)
                    if not n.left.left and not n.left.right:
                        result += n.left.val
                if n.right:
                    temp.append(n.right)

            if len(temp) == 0:
                return result
            else:
                s = temp
