# 201. Bitwise AND of Numbers Range

# 1. Get the list [1, 2, 4, ...]
# 2. Decompose m and n
# 3. Find the unchanged bit.

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0:
            return 0

        l = [2 ** i for i in range(32)]
        l_m = []
        l_n = []
        for i in l[::-1]:
            if m >= i:
                m = m % i
                l_m.append(i)
            if n >= i:
                n = n % i
                l_n.append(i)
 
        result = 0
        for i in range(min(len(l_m), len(l_n))):
            if l_m[i] == l_n[i]:
                result += l_n[i]
            else:
                break
 
        return result
