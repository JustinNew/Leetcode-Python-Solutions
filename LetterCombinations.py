class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        result = []
        l = len(digits) 
        temp = []

        self.util(digits, 0, l, temp, result, d)

        return result

    def util(self, digits, i, l, temp, result, d):
        if i == l:
            s = ''.join(temp)
            result.append(s)
            return

        t = digits[i]
        a = d[t]
        for j in a:
            self.util(digits, i+1, l, temp+[j], result, d)

if __name__=='__main__':

    a = '23'
    so = Solution()

    print (so.letterCombinations(a))
