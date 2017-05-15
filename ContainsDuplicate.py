class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False       
 
        duplicate = {}

        for i in range(len(nums)):
            if nums[i] in duplicate:
                if i - duplicate[nums[i]] <= k:
                    return True

            duplicate[nums[i]] = i

        return False
