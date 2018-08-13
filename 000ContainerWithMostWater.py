# 11. Container With Most Water

# time o(n)
# Key: the water is determined by the shorter one.
# Two points, one from beginning, one from end, move the shorter one and record the MaxWater.

# The intuition behind this approach is that the area formed between 
# the lines will always be limited by the height of the shorter line. 
# Further, the farther the lines, the more will be the area obtained.

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxWater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            water = (right - left) * min(height[right], height[left])
            maxWater = max(maxWater, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater

if __name__ == '__main__':

    s = Solution()
    print (s.maxArea([1,3,2,4,5]))
