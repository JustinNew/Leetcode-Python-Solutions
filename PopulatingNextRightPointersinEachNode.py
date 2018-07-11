# 116. Populating Next Right Pointers in Each Node

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root:
            return

        s = []
        s.append(root)

        while 1:
            temp = []

            for i in range(len(s)):
                if s[i].left:
                    temp.append(s[i].left)
                if s[i].right:
                    temp.append(s[i].right)
                if i + 1 < len(s):
                    s[i].next = s[i + 1]
               
            if len(temp) == 0:
                return 
            else:
                s = temp 
