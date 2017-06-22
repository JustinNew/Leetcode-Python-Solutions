class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = []
        temp = []

        self.util(0, 0, n, n*2, temp, result)
    
        return result

    def util(self, ndx, i, j, n, temp, result):

        if ndx == n:
            result.append(''.join(temp))
            return

        if i == 0 and j > 0:
            self.util(ndx+1, i+1, j-1, n, temp+['('], result)
        else:
            if j == 0: 
                self.util(ndx+1, i-1, j, n, temp+[')'], result)
            else:
                self.util(ndx+1, i+1, j-1, n, temp+['('], result)
                self.util(ndx+1, i-1, j, n, temp+[')'], result)

if __name__=='__main__':

    so = Solution()

    print (so.generateParenthesis(5))
