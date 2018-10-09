# 166. Fraction to Recurring Decimal

# A lot of edge cases.

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if denominator == 0:
            return float('inf')
        elif denominator == 1:
            return str(numerator)
        elif numerator == 0:
            return '0'

        flag = 0
        if numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        elif numerator < 0:
            numerator *= -1 
            flag = 1
        elif denominator < 0:
            denominator *= -1
            flag = 1
        
        if numerator >= denominator:
            p1 = str(int(numerator / denominator))
            numerator %= denominator
            if numerator == 0:
                if flag:
                    return '-' + p1
                else:
                    return p1
        else:
            p1 = str(0)
 
        n = []
        res = []
        while numerator != 0:

            if numerator in n:
                ndx = n.index(numerator)
                if flag:
                    return  '-' + p1 + '.' + ''.join(res[:ndx]) + '(' + ''.join(res[ndx:]) + ')'
                else:
                    return p1 + '.' + ''.join(res[:ndx]) + '(' + ''.join(res[ndx:]) + ')'

            while numerator * 10 < denominator:
                n.append(numerator)
                res.append('0')
                numerator *= 10
                
            n.append(numerator)
            numerator *= 10
            res.append(str(int(numerator / denominator)))
            numerator %= denominator
 
        if flag:
            return '-' + p1 + '.' + ''.join(res) 
        else:
            return p1 + '.' + ''.join(res)
