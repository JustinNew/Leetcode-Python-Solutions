# 8. String to Integer (atoi)

# All kinds of test cases.

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        
        result = []
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        
        flag = 1
        started = 0
        while i < len(str):
            if str[i] == '-' and started == 0:
                flag = -1
                started = 1
            elif str[i] == '+' and started == 0:
                flag = 1
                started = 1
            elif str[i] in '0123456789':
                if started == 0:
                    started = 1
                result.append(str[i])
            else:
                break
            i += 1
                
        if len(result) == 0:
            return 0
        
        result = int(''.join(result)) * flag
        if result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647
        else:
            return result
