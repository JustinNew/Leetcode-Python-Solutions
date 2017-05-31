# Add without +.

class Solution():

    # This does not work for -1 and 1.
    def Add(self, a,b):
        if b == 0:
            return a

        sum = a^b
        carry = (a&b)<<1

        return self.Add(sum, carry)


    def getSum(self, a, b):

        for i in range(32):
            a, b = a^b, (a&b)<<1
        return a if a & 0x80000000 else a & 0xffffffff

    def getSum2(self, a, b):

        if a == 0:
            return b
        elif b == 0:
            return a
        
        mask = 0xffffffff
        
        # positive's two's complement is itself.
        # so we only need to convert negative
        if a < 0:
            a = ~(a ^ mask)
        if b < 0:
            b = ~(b ^ mask)

        # result stores in a.
        # result is in two's complement format
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

#'''
#Idea: 
#Adding two integers a and b (no matter positive or negative) can always be boiled down into 3 steps: 
#1. convert a and b into two's complements. 
#2. add both two's complements. The result is a new two's complement 
#3. convert the result back to integer 
#
#Two things to note:  
#1. In step 1, the two complements are stored as unsigned 32-bit integers. As we all know, a positive integer's two's complement is itself. A negative integer's two's complement is obtained by flipping every bit of its absolute value then adding 1. 
#2. The magic is that if there is a negative integer n, and its unsigned 32-bit two's complement is m, then m = ~(n ^ 0xffffffff) and n = ~(m ^ 0xffffffff). So using this magic, you can do conversion in step 1 and step 3.
#'''

    def Substract(self, a, b):

        return self.getSum2(a,self.getSum2(~b, 1))


    def Substract2(self, a, b):

        if b == 0:
            return a

        mask = 0xffffffff

        # positive's two's complement is itself.
        # so we only need to convert negative
        if a < 0:
            a = ~(a ^ mask)
        if b < 0:
            b = ~(b ^ mask)

        # result stores in a.
        # result is in two's complement format
        while b != 0:
            a, b = (a ^ b) & mask, (((~a) & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a


if __name__=='__main__':

    a = 1
    b = 9

    s = Solution()

    print s.Add(a,b)
    print s.Substract(b, a)
    print s.Substract2(b,a)
