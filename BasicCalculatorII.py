# 227. Basic Calculator II

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        start = 0
        end = 0
        l = []
        while end < len(s):

            if s[end] in ['+', '-', '*', '/']:
                t = s[start:end]
                l.append(int(t))
                l.append(s[end])
                start = end + 1

            end += 1

        t = s[start:end]
        l.append(int(t))

        def util(l):
            if len(l) == 1:
                return l[0]

            flag = 0
            for i in range(len(l)):
                if l[i] in ['*', '/']:
                    flag = 1
                    break

            if flag == 1:
                if l[i] == '*':
                    return util(l[:i - 1] + [int(l[i - 1] * l[i + 1])] + l[i + 2:])
                if l[i] == '/':
                    return util(l[:i - 1] + [int(l[i - 1] / l[i + 1])] + l[i + 2:])

            result = l[0]
            for i in range(1, len(l)):
                if l[i] == '+':
                    result += l[i + 1]
                if l[i] == '-':
                    result -= l[i + 1]

            return result

        return util(l)
