# 378. Kth Smallest Element in a Sorted Matrix

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result.append(matrix[i][j])
                
        result.sort()
        return result[k - 1]

'''
Since the matrix is sorted, we do not need to put all the elements in heap at one time. 
We can simply pop and put for k times. By observation, if we look at the matrix diagonally, 
we can tell that if we do not pop matrix[i][j], we do not need to put on matrix[i][j + 1] and 
matrix[i + 1][j] since they are bigger.

e.g., given the matrix below:
1 2 4
3 5 7
6 8 9
We put 1 first, then pop 1 and put 2 and 3, then pop 2 and put 4 and 5, then pop 3 and put 6...
'''
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            k -= 1
        return result        
