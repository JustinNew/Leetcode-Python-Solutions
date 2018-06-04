# 241. Different Ways to Add Parentheses

# Divide and Conquer.

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if len(input) == 0:
            return 0

        elements = []

        start = 0
        for i in range(len(input)):
            if input[i] in ['*', '+', '-']:
                elements.append(int(input[start:i]))
                elements.append(input[i])
                start = i + 1

        elements.append(int(input[start:]))
        result = self.util(elements)

        return result

    def util(self, elements):

        if len(elements) == 1:
            return elements

        result = []
        for i in range(len(elements)):
            if elements[i] in ['*', '+', '-']:
                left = self.util(elements[:i])
                right = self.util(elements[i + 1:])
                if elements[i] == '*':
                    temp = [j * k for j in left for k in right]
                elif elements[i] == '+':
                    temp = [j + k for j in left for k in right]
                elif elements[i] == '-':
                    temp = [j - k for j in left for k in right]
                result += temp

        return result
