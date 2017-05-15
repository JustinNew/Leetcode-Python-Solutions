class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l = len(s)

        for i in range(int(l/2)):
            if l%(i+1) == 0:
                if s[:i+1]*int(l/(i+1)) == s:
                    return True
        return False

if __name__=='__main__':

    a = 'aabaaba'
    so = Solution()

    print (so.repeatedSubstringPattern(a))
