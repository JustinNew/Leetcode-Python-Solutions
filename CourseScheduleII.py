# 210. Course Schedule II

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        d = {}
        for i in prerequisites:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]

        visited = [-1 for i in range(numCourses)]

        # DFS
        def dfs(i):
            if visited[i] == 1:
                return False
            elif visited[i] == 0:
                return True
            else:
                visited[i] = 0
                if i in d:
                    for j in d[i]:
                        if dfs(j):
                            return True
                visited[i] = 1
                return False

        for k in range(numCourses):
            if dfs(k):
                return []

        result = list(set([i for i in range(numCourses)]) - set([i for i in d.keys()]))

        # BFS
        while 1:
            for i in d:
                if i not in result:
                    flag = -1
                    for j in d[i]:
                        if j not in result:
                            flag = 1
                    if flag != 1:
                        result.append(i)
            if len(result) == numCourses:
                return result

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        d = {}
        for i in prerequisites:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]

        visited = [-1 for i in range(numCourses)]

        result = []
        # DFS
        def dfs(i):
            if visited[i] == 1:
                return False
            elif visited[i] == 0:
                return True
            else:
                visited[i] = 0
                if i in d:
                    for j in d[i]:
                        if dfs(j):
                            return True
                visited[i] = 1
                result.append(i)
                return False

        for k in range(numCourses):
            if dfs(k):
                return []

        return result
