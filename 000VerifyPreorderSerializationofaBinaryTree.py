# 331. Verify Preorder Serialization of a Binary Tree

class Solution(object):

    # Intuition, recursively solve the problem.
    # Time limit exceeded.
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        import re

        l = re.split(',', preorder)

        def valid(l):
            if len(l) == 0:
                return False
            
            if len(l) == 1 and l[0] == '#':
                return True

            if len(l) != 1 and l[0] == '#':
                return False

            flag = 0
            for i in range(1, len(l)):
                if l[i] == '#': 
                    if valid(l[1:i + 1]) and valid(l[i + 1:]):
                        flag = 1
                        break

            if flag == 1:
                return True
            else:
                return False

        return valid(l)

'''
This is very simple problem if you use stacks. The key here is, when you see two consecutive "#" characters on stack, pop both of them and replace the topmost element on the stack with "#". For example,

preorder = 1,2,3,#,#,#,#

Pass 1: stack = [1]

Pass 2: stack = [1,2]

Pass 3: stack = [1,2,3]

Pass 4: stack = [1,2,3,#]

Pass 5: stack = [1,2,3,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,2,#]

Pass 6: stack = [1,2,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,#]

Pass 7: stack = [1,#,#] -> two #s on top so pop them and replace top with #. -> stack = [#]

If there is only one # on stack at the end of the string then return True else return False.
''' 
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        import re

        l = re.split(',', preorder)
