# 150. Evaluate Reverse Polish Notation

# Use stack

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        s = []

        for i in tokens:

            if i in ['+', '-', '*', '/']:
                second = s.pop()
                first = s.pop()

                if i == '+':
                    res = first + second
                elif i == '-':
                    res = first - second
                elif i == '*':
                    res = first * second
                elif i == '/':
                    res = int(first / second)

                s.append(res)
            else:
                t = int(i)
                s.append(t)

        return s[-1]
