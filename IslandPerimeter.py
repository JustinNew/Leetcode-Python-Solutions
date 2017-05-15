import numpy as np

class Solution():

    def IslandPerimeter(self, a):
        m = len(a[:,0])  # Row number
        n = len(a[0,:])  # Column number

        result = 0
        for i in range(m):
            for j in range(n):
                if a[i,j] == 1:
                    result += 4

                    if i-1>=0 and a[i-1,j]==1:
                        result -= 1
                    if i+1<m and a[i+1,j]==1:
                        result -= 1
                    if j-1>=0 and a[i,j-1]==1:
                        result -= 1
                    if j+1<n and a [i,j+1]==1:
                        result -= 1

        return result

    def IslandPerimeter2(self, a):
        m = len(a)  # Row number
        n = len(a[0])  # Column number

        result = 0
        for i in range(m):
            for j in range(n):
                if a[i][j] == 1:
                    result += 4

                    if i-1>=0 and a[i-1][j]==1:
                        result -= 1
                    if i+1<m and a[i+1][j]==1:
                        result -= 1
                    if j-1>=0 and a[i][j-1]==1:
                        result -= 1
                    if j+1<n and a [i][j+1]==1:
                        result -= 1

        return result


if __name__=='__main__':
 
    a = np.array([[0,1,0,0],  [1,1,1,0],  [0,1,0,0],  [1,1,0,0]])
    b = [[0,1,0,0],  [1,1,1,0],  [0,1,0,0],  [1,1,0,0]]

    s = Solution()
    result = s.IslandPerimeter(a)
    result2 = s.IslandPerimeter2(b)
  
    print 'The island perimeter is %d.'%result  
    print 'The island perimeter is %d.'%result2    
