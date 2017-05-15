class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = ['a','e','i','o','u']
        l = []
        result = ''
        for i in s:
            if i in vowel:
                l.append(i)

        for i in range(len(s)):
            if s[i] in vowel:
                result += l.pop()
            else: 
                result += s[i]

        return result

if __name__=='__main__':

    so = Solution()
    print (so.reverseVowels('hello'))
