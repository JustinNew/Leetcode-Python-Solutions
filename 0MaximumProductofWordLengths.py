# 318. Maximum Product of Word Lengths

'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
'''

# My intuition solubtion is o(n^2)
# The good solubtion is still o(n^2) but making great reduction of computation.

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if (not set(words[i]) & set(words[j])) and (len(words[i]) * len(words[j]) >  result):
                    result = len(words[i]) * len(words[j])
 
        return result

    # Improve of my own intuition solution
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for i in words:
            key = tuple(set(sorted(i)))
            d[key] = max(d.get(key, 0), len(i))

        result = 0
        for i in d.keys():
            for j in d.keys():
                if not set(i) & set(j): 
                    result = max(result, d[i] * d[j])

        return result


    # From Leetcode Discussion
    # Use binary representation for each word
    # Get a dictionary for each of the word set
    # Still n^2
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
