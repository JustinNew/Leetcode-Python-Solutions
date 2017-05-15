class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        leftMax = []
        rightMax = []
        water = 0

        m = 0
        for i in range(len(height)):
            m = max(m, height[i])
            leftMax.append(m)

        m = 0
        for i in range(len(height)-1, -1, -1):
            m = max(m, height[i])
            rightMax.append(m)

        rightMax = rightMax[::-1]

        for i in range(len(height)):
            t = min(leftMax[i],rightMax[i])
            if t > height[i]:
                water += t - height[i]

        return water
