class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True
           
        h_l = self.height(root.left, 0)
        h_r = self.height(root.right, 0)

        if abs(h_l - h_r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

    def height(self, root, ht):

        if root==None:
            return ht

        ht_l = self.height(root.left, ht+1)
        ht_r = self.height(root.right, ht+1)

        return max(ht_l, ht_r)
