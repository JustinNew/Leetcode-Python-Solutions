class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i in range(len(s)):
            c = s[i]
            if s.count(c)==1:
                return i

        return -1

    def firstUniqChar2(self, s):

        from collections import Counter
        sc = Counter(s)
        for i in range(len(s)):
            c = s[i]
            if sc.get(c,0)==1:
                return i

        return -1

    def firstUniqChar3(self, s):

        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        for i in range(len(s)):
            c = s[i]
            if d[c]==1:
                return i

        return -1 

if __name__=='__main__':

    s = 'ajdfladfjhhldhafhdahslewhhfadh'

    so = Solution()
    print (so.firstUniqChar(s))
