# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []

        result = []
        stack = []
        stack.append((root, False))

        while stack:
            cur, flag = stack.pop()
            if cur:
                if flag == True:
                    result.append(cur.val)
                else:
                    stack.append(cur, True)
                    stack.append(cur.right, False)
                    stack.append(cur.left, False)

        return result


# We know that a node is visited immediately after it's right child node be visited,
# or it's left child node when it has no right child.
# So:
# Push root in stack.
# While the stack is not empty:
# If the top node of the stack is a leaf node, or the last visited node
# is his right child (or his left child), than pop this node, and visit it.
#Else, push this node's right child and left child into stack.
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

# The 2nd uses modified preorder (right subtree first). Then reverse the result.
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]
