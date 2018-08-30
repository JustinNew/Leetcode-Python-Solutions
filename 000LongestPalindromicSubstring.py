# 5. Longest Palindromic Substring

# Dynamic Programming does not work

class Solution:
    ########################################################################################################################
    '''
    Intuition: from middle to two ends
    '''
    def longestPalindrome(self, s):

        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

    ########################################################################################################################
    '''
    Basic thought is simple. when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2, 
    and that new maxPalindrome includes this new character.
    '''
    def longestPalindrome2(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]

if __name__ == '__main__':

    so = Solution()
    print(so.longestPalindrome('ababababababa'))
