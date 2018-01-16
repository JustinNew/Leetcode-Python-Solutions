# Pour Water.
# The problem is very hard to understand.
# Once totally understand, it's easy to implement the solution with intuition one.

class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        
        while V > 0:
            V -= 1
            flag = 0
            
            best = K
            for i in range(K-1, -1, -1):
                if heights[i] < heights[i+1]:
                    best = i
                    flag = 1
                elif heights[i] > heights[i+1]:
                    break;
                    
            if flag == 0:         
                for i in range(K+1, len(heights)):
                    if heights[i] < heights[i-1]:
                        best = i
                    elif heights[i] > heights[i-1]:
                        break;

            if best != K:
                heights[best] += 1
            else:
                heights[K] += 1           
                    
        return (heights)
        
        
if __name__ == '__main__':
    
    # begin
    s = Solution()
    print (s.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1], 2, 5))
