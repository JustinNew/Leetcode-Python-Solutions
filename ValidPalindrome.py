# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        if len(s) == 0:
            return True
        
        l = re.findall(r'[0-9a-zA-Z]', s)
        s = ''.join(l).lower()
        
        return s == s[::-1]
