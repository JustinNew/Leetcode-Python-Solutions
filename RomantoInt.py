# Convert Roman numbers to Integers.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        d_r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        exceptions = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        i = 0
        result = 0
        while i<len(s):
            c = str[i]
            if i+2 <= len(s):
                two = str[i:i+2]
            else:
                two = None 
            if two in exceptions:
                    result += exceptions[two]
                    i += 2
            elif c in d_r:
                result += d_r[c]
                i += 1
            else:
                print ('It is not Roman numbers.', str)
                return

        return result

    def romanToInt2(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

if __name__=='__main__':
  
        str = 'MMXIV'

        so = Solution()
        print (so.romanToInt(str))
