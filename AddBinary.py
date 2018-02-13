# 7. Add Binary
# Facebook Tage

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        result = ''

        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        carry = 0
        if len(a) < len(b):
            a, b = b, a


        for i in range(len(b)):
            sum = int(b[len(b) - 1 - i]) + int(a[len(a) - 1 - i]) + carry
            carry = int(sum / 2)
            temp = sum % 2      
            result += str(temp)

        for i in range(len(b), len(a)):
            sum = int(a[len(a) - 1 - i]) + carry
            carry = int(sum / 2)
            temp = sum % 2
            result += str(temp)  

        if carry != 0:
            result += str(carry) 

        return result[::-1]
