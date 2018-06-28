# 647. Palindromic Substrings

class Solution:

    # Intuition solution

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0

        def isPal(s):

            return s == s[::-1]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPal(s[i:j+1]):
                    result += 1

        return result 

'''
A DP solution to this problem is to build a table with all possible string[start:end] combinations, storing which are palindromes and which are not (True or False). At any given moment, when you're checking if string[i:j] is a palindrome, you only need to know two things:

Is string[i] equal to string[j]?
Is string[i+1:j-1] a palindrome?

For condition (1), a simple check might do, for condition (2), you use the table. If both conditions are met, mark table[i][j] as True and increase your count.
'''
