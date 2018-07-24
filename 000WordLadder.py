# 127. Word Ladder

class Solution(object):
    # Time Limit Exceeded.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0

        result = 1
        used = [0 for i in range(len(wordList))]

        def getDiff(word1, word2):
            diff = 0
            for k in range(len(word1)):
                if word1[k] != word2[k]:
                    diff += 1
            return diff

        candidate = [beginWord]
        while 1:
            temp = []
            for w in candidate:
                for i in range(len(wordList)):
                    if used[i] == 0:
                        if getDiff(wordList[i], w) == 1:
                            temp.append(wordList[i])
                            used[i] = 1
            result += 1
            if len(temp) == 0:
                return 0
            if endWord in temp:
                return result
            candidate = temp

    # Time Limit Exceeded.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        result = 1
        used = [0 for i in range(len(wordList))]

        candidate = [beginWord]
        while 1:
            temp = []
            for w in candidate:
                for i in range(len(wordList)):
                    if used[i] == 0:
                        if sum([1 for k, l in zip(w, wordList[i]) if k != l]) == 1:
                            temp.append(wordList[i])
                            used[i] = 1
            result += 1
            if len(temp) == 0:
                return 0
            if endWord in temp:
                return result
            candidate = temp

    # Two end BFS
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
