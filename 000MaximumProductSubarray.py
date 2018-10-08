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
# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tMax = nums[0]
        curMax = nums[0]
        tMin = nums[0]
        curMin = nums[0]

        l = len(nums)
        if l == 1:
            return tMax

        for i in range(1, l):
            t1 = max(nums[i], curMax * nums[i], curMin * nums[i])
            t2 = min(nums[i], curMin * nums[i], curMax * nums[i])
            curMax, curMin = t1, t2

            tMax = max(tMax, curMax)

        return tMax
