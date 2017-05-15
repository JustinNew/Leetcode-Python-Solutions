class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        c = Counter(s)

        re = 0
        flag = 0
        for i in set(s):
            re += c.get(i,0)/2
            if c.get(i,0)%2 == 1:
                flag = 1

        if flag==1:
            return re*2+1
        else:
            return re*2
