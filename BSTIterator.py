# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nums = []
        self.stack = []

        self.stack.append((root, False))
        while self.stack:
            node, flag = self.stack.pop()
            if node:
                if flag:
                    self.nums.append(node.val)
                else:
                    self.stack.append((node.right, False))
                    self.stack.append((node, True))
                    self.stack.append((node.left, False))

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.nums)>0:
            return True
        else: 
            return False

    def next(self):
        """
        :rtype: int
        """
        return self.nums.pop(0)
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
