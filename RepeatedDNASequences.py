# 187. Repeated DNA Sequences

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        l = len(s)
        if l < 10:
            return []

        result = {}
        for i in range(l - 9):
            t = s[i:i + 10]
            if t in result:
                result[t] += 1
            else:
                result[t] = 1

        return [key for key, value in result.items() if value > 1]

if __name__ == '__main__':

    s = Solution()
    print(s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
