# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # This can easily be modified to do preorde, inorder and postorder traversal.
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result, stack = [], [(root, False)]

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    result.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return result

    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            # Key is examine before put in.
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    # DFS Recursion.
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        if root:
            self.util(root, result)
            return result
        else:
            return []

    def util(self, root, result):

        if root.left:
            self.util(root.left, result)

        result += [root.val]

        if root.right:
            self.util(root.right, result)

        return

    # Using Stack, and a visited FLAG.
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        s = []
        result = []
        if root:
            s.append((root,False))

        while len(s) != 0:
            (cur, flag) = s.pop()
            if flag == False:
                if cur.right:
                    s.append((cur.right, False))
                s.append((cur, True))
                if cur.left: 
                    s.append((cur.left, False))
            else:
                result += [cur.val]

        return result

        
        
        
