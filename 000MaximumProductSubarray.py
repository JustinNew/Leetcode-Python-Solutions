# 152. Maximum Product Subarray

# This is very similar to '53. Maximum Subarray'. 
# Since negative changes sign, so the max can be Min*curr(negative curr) or Max*curr(positive curr).
# Need to tract both Min and Max

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curMax = nums[0]
        curMin = nums[0]
        totMax = nums[0]

        for i in range(1, len(nums)):
            if nums[i] >= 0:
                curMax, curMin = max(nums[i], curMax * nums[i]), min(nums[i], curMin * nums[i])
            else:
                curMax, curMin = max(nums[i], curMin * nums[i]), min(nums[i], curMax * nums[i])

            totMax = max(totMax, curMax)

        return totMax
