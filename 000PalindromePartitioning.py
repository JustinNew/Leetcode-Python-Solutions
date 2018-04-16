# 131. Palindrome Partitioning

# Divide and Conquer.
# Trick how to avoid repeated partition: just further partition the right-half.

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]

        result = []
        if s == s[::-1]:
            result.append([s])

        for i in range(1, len(s)):
            t = s[:i]
            if t == t[::-1]:
                left = [s[:i]]
                right = self.partition(s[i:])

                for j in range(len(right)):
                    result.append(left + right[j])

        return result

if __name__ == '__main__':

    s = Solution()
    print(s.partition('aaa'))
