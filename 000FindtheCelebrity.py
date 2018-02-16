# 277. Find the Celebrity
# Facebook Tag
# Logic needs to be very clear.
# Test some cases.

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        cel = set([i for i in range(n)])
        non = set()
        visited = [0 for i in range(n)]

        while True:

            for i in range(n):
                
                if visited[i] == 0:
   
                    flag = 0
                    for j in cel:
                        if i != j and knows(i, j):
                            flag = 1
                            break

                    if flag == 0 and len(non) != 0:
                        for j in non:
                            if knows(i,j):
                                flag = 1
                                break

                    if flag == 1:
                        non = non | set([i])
                        cel = cel - set([i])

                    visited[i] = 1

            if sum(visited) == n:
                if len(cel) == 1:
                    for i in cel:
                        for j in non:
                            if knows(i,j) or not knows(j,i):
                                return -1
                        return i

                return -1 
