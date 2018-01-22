# 43 Multiply String

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # Change to number.
        base = []
        multiplier = []
        for i in range(len(num1) - 1, -1, -1):
            t = ord(num1[i]) - ord('0')
            base.append(t)

        for i in range(len(num2) - 1, -1, -1):
            t = ord(num2[i]) - ord('0')
            multiplier.append(t)

        if len(multiplier) == 1 and multiplier[0] == 0:
            return '0'
        if len(base) == 1 and base[0] == 0:
            return '0'

        if len(multiplier) > len(base):
            base, multiplier = multiplier, base

        result = [0 for i in range(len(num1) + len(num2))]
        for j in range(len(multiplier)):
            carry = 0
            for i in range(len(base)):
                temp = result[i+j] + carry + multiplier[j] * base[i]
                result[i+j] = temp % 10
                carry = int(temp / 10)
            if carry != 0:
                result[i+j+1] = result[i+j+1] + carry

        while result[-1] == 0:
            result.pop()

        l = []
        for i in range(len(result) - 1, -1, -1):
            l.append(chr(result[i] + ord('0')))

        return ''.join(l)

if __name__ == '__main__':

    s = Solution()
    print (s.multiply('99', '9'))
