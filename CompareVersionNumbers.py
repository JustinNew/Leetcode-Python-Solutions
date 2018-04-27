# 165. Compare Version Numbers

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        if not version1 and not version2:
            return 0
        elif not version1:
            return -1
        elif not version2:
            return 1

        v1 = version1.split('.')
        v2 = version2.split('.')

        for i in range(len(v1)):
            v1[i] = int(v1[i])

        for i in range(len(v2)):
            v2[i] = int(v2[i])

        count = 0
        for i in range(len(v1) - 1, 0, -1):
            if v1[i] == 0:
                count += 1
            else:
                break

        for i in range(count):
            v1.pop()

        count = 0
        for i in range(len(v2) - 1, 0, -1):
            if v2[i] == 0:
                count += 1
            else:
                break

        for i in range(count):
            v2.pop()

        l = min(len(v1), len(v2))
        for i in range(l):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        if len(v1) == len(v2):
            return 0
        elif len(v1) == l:
            return -1
        elif len(v2) == l:
            return 1
