class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif self.isPair(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])

        if len(stack) != 0:
            return False
        else: 
            return True

    def isPair(self, s, t):

        if s == '(' and t == ')':
            return True
        if s == '[' and t == ']':
            return True
        if s == '{' and t == '}':
            return True

        return False
