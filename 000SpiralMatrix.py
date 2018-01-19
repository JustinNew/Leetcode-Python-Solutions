# Leetcode 54 Spiral Matrix
# Extremely Error prone, have to be really careful.

# Go by circle to print out, except only one row or one column left

# Take care of case when one row or one column left

# Go by circle: go right, go down, go left, and go up
# r++, r--, c++, c-- as steps down/up, right/left
# m, n are the bound. How many steps to go in each direction.
# After each circle finished, the other dimension reduced by 2.
# Pay attention to the initial step r = 0, c = 0 and r++ , c++ after each circle.
# Pay attention to c++/c--, r++/r-- first before print out element.

# Pay attention to m > 0 and n > 0.
# The corner cases: [], [1,2,3], [[1,2,3]]

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        m = len(matrix)
        if m == 0:
            return []      
        elif type(matrix[0]) is list: 
            n = len(matrix[0]) 
        else:
            return matrix
            
        r = 0
        c = 0

        while m > 0 and n > 0:
            
            if m == 1:
                for i in range(n):
                    result.append(matrix[r][c])
                    c += 1
                break
            elif n == 1:
                for i in range(m):
                    result.append(matrix[r][c])
                    r += 1
                break
                    
            # Process a circle
            # Go right
            for i in range(n-1):
                result.append(matrix[r][c])
                c += 1

            # Go down
            for i in range(m-1):
                result.append(matrix[r][c])
                r += 1

            # Go left
            for i in range(n-1):
                result.append(matrix[r][c])
                c -= 1
            
            # Go up
            for i in range(m-1):
                result.append(matrix[r][c])
                r -= 1
            
            r += 1
            c += 1
            m -= 2    
            n -= 2

        return result
           

if __name__ == '__main__':

    s = Solution()
    print (s.spiralOrder([[1],[3],[5]])) 
