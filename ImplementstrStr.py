# 28. Implement strStr()

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0 and len(needle) != 0:
            return -1

        if len(haystack) != 0 and len(needle) == 0:
            return 0
        
        if len(haystack) == 0 and len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            matched = 1
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    matched = -1

            if matched == 1:
                return i

        return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(haystack) == 0 and len(needle) != 0:
            return -1

        if len(haystack) != 0 and len(needle) == 0:
            return 0
        
        if len(haystack) == 0 and len(needle) == 0:
            return 0

        if needle not in haystack:
            return -1
        
        return haystack.index(needle)

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(haystack) == 0 and len(needle) != 0:
            return -1

        if len(haystack) != 0 and len(needle) == 0:
            return 0
        
        if len(haystack) == 0 and len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i
            
        return -1 
