# Find the difference in two strings.

class Solution():

    def Difference(self, s, t):
    
        l = {}
        for i in range(len(t)):
            if t[i] in l.keys():
                l[t[i]] = l[t[i]] + 1
            else:
                l[t[i]] = 1            

        for i in range(len(s)):
            l[s[i]] = l[s[i]] - 1

        for m in l.keys():
            if l[m] != 0:
                result = m

        return result

    def Difference2(self, s, t):
        for i in t:
            if t.count(i) != s.count(i):
            return i

    def findTheDifference(self, s, t):
        for ch in t:
            if (s+t).count(ch)%2:
                return ch;

    def findTheDifference2(self, s, t):
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)


    def findTheDifference3(self, s, t):
        k = 0
        for i in range(len(s)):
            k -= ord(s[i])
            k += ord(t[i])
            
        k+=ord(t[-1])
        return chr(k)

    def findTheDifference4(self, s, t):
        return chr(reduce(operator.xor, map(ord, s + t)))

if __name__=='__main__':

    s = 'abcd'
    t = 'abcde'

    so = Solution()

    print 'First method:', so.Difference(s, t)
    print 'Second method:', so.Difference2(s, t)
