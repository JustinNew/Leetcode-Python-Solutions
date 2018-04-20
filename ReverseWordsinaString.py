# 151. Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = s.strip().split()
        l = l[::-1]
        return ' '.join(l)

if __name__ == '__main__':

    s = Solution()
    print(s.reverseWords('the sky is blue'))
