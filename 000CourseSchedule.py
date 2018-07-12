# 207. Course Schedule

# To see whether there is circle in the graph.
# 1. if node v has not been visited, then mark it as 0.
# 2. if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# 3. if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True

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
