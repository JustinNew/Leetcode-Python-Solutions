class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys

        nums = sorted(nums)

        if len(nums) <= 2:
            return 0 

        result = 0 

        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum < target:
                    result += 1

                if sum > target:
                    end -= 1
                else: 
                    start += 1

        return result
