class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        import math
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        result = 0
        for i in range(len(num2)):
            multiplier = math.pow(10,i)
            temp = 0
            digit = int(num2[i])
            for j in range(len(num1)):
                t = int(num1[j])
                t_m = math.pow(10,j)
                temp += t*digit*t_m
            result += temp*multiplier
        
        return str(int(result))

if __name__=='__main__':

    so = Solution()
    print (so.multiply('999','987'))
