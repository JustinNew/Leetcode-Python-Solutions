# 74. Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])
  
        low = 0 
        high = m * n - 1

        while low <= high:

            mid = int((high + low) / 2)
            row = int(mid / n)
            column = mid - row * n
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False

# Find an int in an increasing Matrix.
# Row increase from left to right.
# Column increase from top to bottom.
import numpy as np

def Search1(a,v):
    m = len(a[:,0])
    n = len(a[0,:])

    i = 0
    j = m-1
    while i<=j:
        mid = (i+j)/2
        if a[mid,n-1]==v:
            print 'Find value:', mid, n-1
            return
        elif a[mid,n-1]>v:
            j=mid-1
        else:
            i=mid+1

    l = 0
    k = n-1
    while l<=k:
        mid = (l+k)/2
        if a[i,mid]==v:
            print 'Find value:', i, mid
            return
        elif a[i,mid]>v:
            k = mid-1
        else:
            l = mid+1

    print 'Value is not found.'
    return

def Search2(a,v):
    m = len(a[:,0])
    n = len(a[0,:])

    low = 0
    high = m*n-1

    while low<=high:
        mid = (low+high)/2
        row = GetRow(mid,m,n)
        col = GetCol(mid,m,n)

        if v==a[row][col]:
            print 'Find value at %d,%d'%(row,col)
            return
        elif v<a[row][col]:
            high = mid - 1
        else:
            low = mid + 1    

    print 'Value is not found.'

    return

def GetRow(mid, m, n):
    return (mid/n)

def GetCol(mid,m,n):
    return (mid%n)-1

if __name__ == '__main__':
    a = np.array([[1,3,5,7,9],[10,12,14,16,18],[19,21,23,25,27],[28,30,32,34,36]])
    v = 30
    Search1(a,v)
    Search2(a,v)
