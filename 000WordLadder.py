# 127. Word Ladder

class Solution:

    # BFS: level order traversal
    # Time Limit Exceeded
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0

        count = 1
        candidate = [beginWord]
        d = {w:0 for w in wordList}

        while 1:

            count += 1
            temp = []
            for w in candidate:
                for i in range(len(w)):
                    for s in 'abcdefghijklmnopqrstuvwxyz':
                        t = w[:i] + s + w[i + 1:]
                        if t == endWord:
                            return count
                        elif t in wordList and d[t] == 0:
                            temp.append(t)
                            d[t] = 1

            if not temp:
                return 0

            candidate = temp

    # Use set and passed.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        count = 1
        candidate = [beginWord]

        while 1:

            count += 1
            temp = []
            for w in candidate:
                for i in range(len(w)):
                    for s in 'abcdefghijklmnopqrstuvwxyz':
                        t = w[:i] + s + w[i + 1:]
                        if t == endWord:
                            return count
                        elif t in wordList:
                            temp.append(t)
                            wordList.remove(t)

            if not temp:
                return 0

            candidate = temp


    # From Discussion, use set.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
