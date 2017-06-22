# Using two pointers.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        if sum(nums) < s:
            return 0
        if sum(nums) == s:
            return len(nums)

        currSum = nums[0]
        if currSum >= s:
            return 1

        cnt = len(nums)
        i = 0
        j = 1
        while j < len(nums):
            currSum += nums[j]
            if currSum >= s:
                while currSum - nums[i] >= s:
                    currSum -= nums[i]
                    i = i + 1
                t = j - i + 1
                cnt = min(cnt, t)
            j += 1

        return cnt
