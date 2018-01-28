# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return None

        maxSum = nums[0]
        currentSum =nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(currentSum, maxSum)

        return maxSum

if __name__ == '__main__':

    s = Solution()
    print (s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
