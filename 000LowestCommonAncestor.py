# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # This works only when p and q are both guaranteed to be in the tree.
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


class Solution:

    def lowestCommonAncestor(self, root, p, q):
    
        # Find Ancestors for p and q.
        p = self._dfs(root, p)
        q = self._dfs(root, q)

        # Get the lowest common ancestors.
        answer = root
        while p and q and p[-1] is q.pop():
            answer = p.pop()
        return answer

    def _dfs(self, root, n):

        # Build a parent dictionary for look up.
        parents = dict()

        # DFS to build up and dictionary.
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node is n:
                break
            stack.append(node.left)
            stack.append(node.right)
            parents[node.left] = node
            parents[node.right] = node

        # Build up the ancestors.
        answer = [n]
        while answer[-1] != root:
            answer.append(parents[answer[-1]])

        return answer
