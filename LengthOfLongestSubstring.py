class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
 
        if len(s) == 0:
            return 0

        start = 0
        d = {}
        d[s[0]] = 1
        ml = 1

        for i in range(1,len(s)):
            print (d)
            while d.get(s[i],0) != 0:
                d[s[start]] -= 1
                start += 1
            if i - start + 1 > ml:
                ml = i - start + 1            

            d[s[i]] = 1

        return ml

if __name__=='__main__':

    so = Solution()

    print (so.lengthOfLongestSubstring('jlygy'))
