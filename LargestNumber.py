# Leetcode 747
# Largest Number At Least Twice of Others
# Different corner cases.

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0
        else:
            if nums[1] < nums[0]:            
                largest = 0
                second = 1
            else:
                largest = 1
                second = 0

            for i in range(2, len(nums)):
                if nums[i] > nums[largest]:
                    second = largest
                    largest = i
                elif nums[i] > nums[second]:
                    second = i

            if nums[largest] >= 2 * nums[second]:
                return largest
            else:
                return -1
        
