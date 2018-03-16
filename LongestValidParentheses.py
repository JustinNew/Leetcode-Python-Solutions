# 32. Longest Valid Parentheses
# Travel the string twice to solve the problem.
# 1st travel to label not paired parentheses.
# 2nd travel to get the longest paired parentheses.
# Using stack for parentheses.

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        current = 0
        stack = []
        notpaired = {}

        for i in range(len(s)):

            if len(stack) == 0:
                stack.append((i, s[i]))
            else:
                (t, peek) = stack[-1]
                if s[i] == ')' and peek == '(':
                    stack.pop()
                else:
                    stack.append((i, s[i]))

        for (t, peek) in stack:
            notpaired[t] = 1

        for i in range(len(s)):

            if i in notpaired:
                result = max(result, current)
                current = 0
            else:
                current += 1

        result = max(result, current)

        return result

if __name__ == '__main__':

    s = Solution()
    print(s.longestValidParentheses("(()))(()()()("))
