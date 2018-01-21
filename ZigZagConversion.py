# 6 ZigZag Conversion
# A lot of similarity with '54 Spiral Matrix'

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
	
        r = numRows
        c = len(s)
        k = 0
        l = len(s)
		
        if c == 0:
            return ''
        elif r == 1:
            return s
        else:
            result = [['' for j in range(c)] for i in range(r)]
            ri = 0
            ci = 0
            
            while k < l:
                # Go down first.
                for i in range(0, r-1):
                    if k < l:
                        result[ri][ci] = s[k]
                        k += 1
                        ri += 1
                    else:
                        break
                    
                # Go up triangle.
                for i in range(0, r-1):
                    if k < l:
                        result[ri][ci] = s[k]
                        k += 1
                        ri -= 1
                        ci += 1
                    else:
                        break

        value = ''
        for i in range(r):
            value += ''.join(result[i])
                
        return value
            
if __name__ == '__main__':
    
    s = Solution()
    print (s.convert('abcd', 3))                    
