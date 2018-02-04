# 89. Grey Code

# Good analysis is needed. 
# Start from i = 1, 2, 3, .., try to get a solution.

class Solution:
    # @return a list of integers
    '''
    from up to down, then left to right
    
    0   1   11  110
            10  111
                101
                100
                
    start:      [0]
    i = 0:      [0, 1]
    i = 1:      [0, 1, 3, 2]
    i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
    '''
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results
