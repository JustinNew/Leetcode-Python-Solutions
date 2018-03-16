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

    # Dynamics Programming. 
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in xrange(len(s))]
        max_to_now = 0
        for i in xrange(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (()) 
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid 
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now

if __name__ == '__main__':

    s = Solution()
    print(s.longestValidParentheses("(()))(()()()("))
