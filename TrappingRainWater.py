# 42. Trapping Rain Water

'''
For each position, the trapped water is detremined by the min(leftMax, rightMax).
'''

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 2:
            return 0

        leftMax = [0 for i in range(len(height))]
        rightMax = [0 for i in range(len(height))]

        curMax = 0
        for i in range(len(height) - 1):
            curMax = max(height[i], curMax)
            leftMax[i + 1] = curMax

        curMax = 0
        for i in range(len(height) - 1, 0, -1):
            curMax = max(height[i], curMax)
            rightMax[i - 1] = curMax

        result = 0
        for i in range(len(height)):
            result += max(0, min(leftMax[i], rightMax[i]) - height[i])

        return result
