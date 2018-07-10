# 76. Minimum Window Substring

# Two pointers.

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) == 0:
            return ''
        elif len(t) > len(s):
            return ''

        m = {}
        for i in t:
            if i in m: 
                m[i] += 1
            else:
                m[i] = 1

        def largeD(d, m):
            for i in m:
                if d[i] < m[i]:
                    return False
            return True

        d = {k:0 for k,v in m.items()}
        start = 0
        end = 0
        result = ''
        while end < len(s):
            if s[end] in m:
                d[s[end]] += 1
                if largeD(d, m):
                    if (len(result) == 0) or (len(result) > end - start + 1):
                        result = s[start: end + 1]
                    while (start < end) and (s[start] not in m or d[s[start]] > m[s[start]]):
                        if s[start] in m:
                            d[s[start]] -= 1
                        start += 1
                    if largeD(d, m) and (len(result) > end - start + 1):
                        result = s[start: end + 1]
            end += 1

        return result                
 
if __name__ == '__main__':

    so = Solution()
    print(so.minWindow('adobecodebanc', 'abc'))
