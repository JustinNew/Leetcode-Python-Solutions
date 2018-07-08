# 395. Longest Substring with At Least K Repeating Characters

# 1. Count the frequency of all the letters
# 2. Recursion:
#    a. remove one letter with frequence < k
#    b. do the count frequence for the remaining two subsets

class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) < k:
            return 0

        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        l = [(k, v) for k, v in d.items()]
        l.sort(key=lambda x: x[1])

        if l[-1][1] < k:
            return 0
        elif l[0][1] >= k:
            return len(s)
        else:
            letter = l[0][0]
            for i in range(len(s)):
                if s[i] == letter:
                    break
            left = self.longestSubstring(s[:i], k)
            right = self.longestSubstring(s[i+1:], k)
            return max(left, right)
