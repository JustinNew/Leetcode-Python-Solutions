# 84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        m = float('inf')
        ndx = 0
        for i in range(len(heights)):
            if heights[i] < m:
                m = heights[i]
                ndx = i

        all = m * len(heights) 
        left = self.largestRectangleArea(heights[:i])
        right = self.largestRectangleArea(heights[i + 1:])

        return max(all, left, right)       

'''
The stack maintain the indexes of buildings with ascending height. 
Before adding a new building pop the building who is taller than the new one. 
The building popped out represent the height of a rectangle with the new building 
as the right boundary and the current stack top as the left boundary. 
Calculate its area and update ans of maximum area. 
Boundary is handled using dummy buildings.

1. Using stack to only keep increasing sequence.
2. When find an element smaller, calculate the rectangle area.
'''

    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
