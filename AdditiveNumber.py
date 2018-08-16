# 306. Additive Number

# DFS
# First number and second number is determined then all the next ones are determined

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        if len(num) <= 2:
            return False

        def add(n1, n2):
            n1 = n1[::-1]
            n2 = n2[::-1]
            if len(n1) < len(n2):
                n1, n2 = n2, n1
            result = ''
            carry = 0
            for i in range(len(n2)):
                s, carry = (int(n1[i]) + int(n2[i]) + carry) % 10, int((int(n1[i]) + int(n2[i]) + carry) / 10)
                result += str(s)
            for j in range(i + 1, len(n1)):
                s, carry = (int(n1[j]) + carry) % 10, int((int(n1[j]) + carry) / 10)
                result += str(s)
            if carry != 0:
                result += str(carry)
            return result[::-1]

        l = len(num)

        for i in range(int(l / 2)):
            for j in range(i + 1, l - i - 1):
                n1 = num[:i + 1]
                if n1[0] == '0' and len(n1) != 1:
                    break
                n2 = num[i + 1:j + 1]
                if n2[0] == '0' and len(n2) != 1:
                    break

                k = j + 1
                flag = 0
                while k < l:
                    n3 = add(n1, n2)
                    m = len(n3)
                    if k + m > l or n3 != num[k:k + m]:
                        flag = 1
                        break
                    
                    k += m
                    n1, n2 = n2, n3
                
                if flag == 0:
                    return True

        return False
