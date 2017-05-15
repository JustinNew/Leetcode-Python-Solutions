class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        l = len(nums)

        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                l = l - 1
            else:
                nums[j] = nums[i]
                j += 1

        return l
