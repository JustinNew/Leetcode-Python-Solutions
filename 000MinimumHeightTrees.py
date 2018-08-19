# 310. Minimum Height Trees

'''
# For a undirected graph with tree characteristics, we can choose any node as the root. 
# The result graph is then a rooted tree. Among all possible rooted trees, 
# those with minimum height are called minimum height trees (MHTs). Given such a graph, 
# write a function to find all the MHTs and return a list of their root labels.

# The graph contains n nodes which are labeled from 0 to n - 1. 
# You will be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

class Solution(object):

    # DFS search
    # Time Limit Exceeded
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if len(edges) == 0:
            return [0]

        # Create connected nodes for each node
        d = {}
        for i in edges:
            d[i[0]] = d.get(i[0], []) + [i[1]]
            d[i[1]] = d.get(i[1], []) + [i[0]]


        def dfs(node, h):
            visited[node] = 1            

            heights = [h]
            for i in d[node]:
                if visited[i] == 0:
                    heights.append(dfs(i, h + 1))
                    visited[i] = 0

            return max(heights)

        # dfs to find the height of a rooted tree
        h = float('inf')
        result = []
        for i in range(n):
            visited = [0 for j in range(n)]
            t = dfs(i, 0)
            if t < h:
                h = t
                result = [i]
            elif t == h:
                result += [i]

        return result

'''
Because there're at most two nodes can be Minimum Height Trees. And all leaves are impossible because such nodes. So we can iterative remove leaves and related edges till we reach 1 or 2.
'''
def findMinHeightTrees(self, n, edges):
    d = collections.defaultdict(set)
    for u, v in edges:
        d[u].add(v)
        d[v].add(u)
    s = set(range(n))
    while len(s) > 2:
        leaves = set(i for i in s if len(d[i]) == 1)
        s -= leaves
        for i in leaves:
            for j in d[i]:
                d[j].remove(i)
    return list(s)
