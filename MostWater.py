class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(nums)<2:
            return 0

        water = 0
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                t = min(nums[i],nums[j])*(j-i)
