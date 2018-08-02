# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Postorder can be accomplised by (modified) preorder:
    # 1. modified preorder (right subtree first) first;
    # 2. reverse result.
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        if not root:
            return []

        s = [root]
        result = []
        while s:
            n = s.pop()
            result.append(n.val)

            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)

        return result[::-1]

    # Use additional flag to indicate whether visited or not for travesal
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        if not root:
            return []

        s = [(root, False)]
        result = []
        while s:
            n, flag = s.pop()
            if flag:
                result.append(n.val)
            else:
                s.append((n, True))
                if n.right:
                    s.append((n.right, False))
                if n.left:
                    s.append((n.left, False))

        return result

# We know that a node is visited immediately after it's right child node be visited,
# or it's left child node when it has no right child.
# So:
# Push root in stack.
# While the stack is not empty:
# If the top node of the stack is a leaf node, or the last visited node
# is his right child (or his left child), than pop this node, and visit it.
# Else, push this node's right child and left child into stack.
# Loop to 2.
# The code:

def postorderTraversal(self, root):
    if root is None: return []
   
    s, lastVist, ret = [root], root, []
    while s:
        top = s[-1]
        if (top.left is None and top.right is None) or \
                (top.right == lastVist or top.left == lastVist):
            lastVist = s.pop()
            ret.append(lastVist.val)
        else:
            if top.right: s.append(top.right)
            if top.left:  s.append(top.left)

    return ret
