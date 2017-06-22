# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# This is very similar to 'MaxSubArray.py'. 
# Since negative changes sign, so the max can be Min*curr(negative curr) or Max*curr(positive curr).
# Need to tract both Min and Max
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        result = nums[0]
        min_list = [0 for i in range(len(nums))]
        max_list = [0 for i in range(len(nums))]
        min_list[0] = nums[0]
        max_list[0] = nums[0]

        for i in range(1,len(nums)):
            min_list[i] = min(min(min_list[i-1]*nums[i],max_list[i-1]*nums[i]),nums[i])
            max_list[i] = max(max(min_list[i-1]*nums[i],max_list[i-1]*nums[i]),nums[i])
            result = max(result, max_list[i])

        return result
