# 150. Evaluate Reverse Polish Notation

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 0:
            return None

        operators = ['+', '-', '*', '/']
        s = []

        for i in tokens:
            if i in operators:
                right = s.pop()
                left = s.pop()
                if i == '+':
                    t = left + right
                elif i == '-':
                    t = left - right
                elif i == '*':
                    t = left * right
                else:
                    if left*right < 0 and left % right != 0:
                        t = left / right + 1
                    else:
                        t = left / right
                s.append(t)
            else:
                s.append(int(i))
                
            print(s[-1])
            
        return s[-1]
