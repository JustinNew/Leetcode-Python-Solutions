# 49. Group Anagrams

class Solution(object):
    # Time Limit Exceeded.
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import Counter

        if len(strs) == 0:
            return []

        result = []
        for word in strs:
            flag = 0
            for list in result:
                if Counter(word) == Counter(list[0]):
                    list.append(word)
                    flag = 1
                    break
            if flag == 0:
                result.append([word])

        return result

    # Use dictionary and get a list for key.
    # Time Limit Exceeded.
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 0:
            return []

        result = []
        keys = []

        def getKey(t_word):
            d = {}
            for i in t_word:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            l = [(k,v) for k, v in d.items()]
            l.sort(key=lambda x: x[0])
            return l

        for word in strs:
            flag = 0
            for i in range(len(result)):
                if getKey(word) == keys[i]:
                    result[i].append(word)
                    flag = 1
                    break
            if flag == 0:
                keys.append(getKey(word))
                result.append([word])

        return result    

    ##########################################################################################################
    # My own solution.
    # Tuple as dictionary key.

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 0:
            return []

        d = {}

        for s in strs:
            k = tuple(sorted(s))
            d[k] = d.get(k, []) + [s]

        return [i for i in d.values()]
