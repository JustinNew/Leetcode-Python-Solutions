# 41. First Missing Positive

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(len(nums)):
            t = abs(nums[i])
            if t >= 1 and t <= n and nums[t - 1] > 0:
                nums[t - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return n + 1
                
