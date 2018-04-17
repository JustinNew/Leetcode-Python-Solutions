# 133. Clone Graph

# Trick: create a dictionary to map old node and new old together. 

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    # BFS
    def cloneGraph(self, node):

        if not node:
            return None

        s = []
        s.append(node)

        new = UndirectedGraphNode(node.label)
        s_n = []
        s_n.append(new)
        dic = {}
        dic[node] = new

        visited = []
        visited.append(node)

        while True:

            n = s.pop()
            n_n = s_n.pop()
    
            for i in n.neighbors:
                if i not in visited:
                    t = UndirectedGraphNode(i.label)
                    dic[i] = t
                    s.append(i)
                    visited.append(i)
                    s_n.append(t)
                n_n.neighbors.append(dic[i])

            if len(s) == 0:
                return new
