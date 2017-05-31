class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return

        start = 0
        end = len(nums) - 1
        while start < end:
            mid = int((start+end)/2)
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
 
        return nums[start]

