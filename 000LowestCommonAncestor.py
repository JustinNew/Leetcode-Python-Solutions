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
            stack.append(node.right)
            stack.append(node.left)
            parents[node.left] = node
            parents[node.right] = node

        # Build up the ancestors.
        answer = [n]
        while answer[-1] != root:
            answer.append(parents[answer[-1]])

        return answer


# DFS to build up the Ancesters.
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        nodes_p = []
        nodes_q = []

        self.dfs(root, p, nodes_p)
        self.dfs(root, q, nodes_q)

        n = None
        i = 0
        while i < len(nodes_p) and i < len(nodes_q):
            if nodes_p[i] == nodes_q[i]:
                n = nodes_p[i]
                i += 1
            else:
                break

        return n

    def dfs(self, root, node, list):

        if not root:
            return False

        if root == node:
            list.append(root)
            return True

        if root.left:
            list.append(root)
            if self.dfs(root.left, node, list):
                return True
            list.pop()

        if root.right:
            list.append(root)
            if self.dfs(root.right, node, list):
                return True
            list.pop()

        return False
