class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return nums

        result = 0
        for i in range(len(nums)):
            result ^= nums[i]

        for i in range(1, len(nums)+1):
            result ^= i

        return result
