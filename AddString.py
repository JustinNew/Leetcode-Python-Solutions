class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = num1[::-1]
        num2 = num2[::-1]

        if len(num1)>len(num2):
            num1, num2 = num2, num1

        result = ''
        carry = 0
        for i in range(len(num1)):

            temp1 = ord(num1[i])-ord('0')
            temp2 = ord(num2[i])-ord('0')

            str = (temp1+temp2+carry)%10
            carry = int((temp1+temp2+carry)/10)

            result += chr(str+ord('0'))

        for j in range(i+1, len(num2)):

            temp1 = ord(num2[j])-ord('0')
            str = (temp1+carry)%10
            carry = int((temp1+carry)/10)
            result += chr(str+ord('0'))

        if carry != 0:
            result += chr(carry+ord('0'))
        
        return result[::-1]

    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        N, M = len(num1), len(num2)
        i,j = N-1, M-1
        result, carry = [], 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                s = int(num1[i]) + int(num2[j]) + carry
                s, carry = s%10, s//10
                result.append(str(s))
                i,j= i-1, j-1 
            elif i >= 0:
                s = int(num1[i]) + carry
                s, carry = s%10, s//10
                result.append(str(s))
                i= i-1 
            elif j >= 0:
                s = int(num2[j]) + carry
                s, carry = s%10, s//10
                result.append(str(s))
                j = j-1 
        if carry:
            result.append(str(carry))
        result.reverse()
        return "".join(result)

if __name__=='__main__':

    a = '99'
    b = '9'

    so = Solution()

    print (so.addStrings(a, b))
