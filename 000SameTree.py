# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True
        elif not q or not p:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def isSameTree(self, p, q):
        # Using BFS
        # Not an easy one
        from collections import deque

        queue_p = deque()
        queue_q = deque()

        queue_p.append(p)
        queue_q.append(q)

        while queue_p and queue_q:
            p_t = queue_p.popleft()
            q_t = queue_q.popleft()

            if not p_t and not q_t:
                next
            elif not p_t or not q_t:
                return False
            else:
                if p_t.val != q_t.val:
                    return False
                if p_t.left and q_t.left:
                    queue_p.append(p_t.left)
                    queue_q.append(q_t.left)
                elif p_t.left or q_t.left:
                    return False
                if p_t.right and q_t.right:
                    queue_p.append(p_t.right)
                    queue_q.append(q_t.right)
                elif p_t.right or q_t.right:
                    return False 

        if not queue_p and not queue_q:
            return True
        elif not queue_p or not queue_q:
            return False   
