# 34. Search for a Range

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1]

        begin = -1
        end = -1

        # Binary Search for Begin
        low = 0
        high = len(nums) - 1
        while low <= high:

            mid = int((high + low)/2)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid == 0:
                    begin = 0
                    break
                elif nums[mid - 1] < target:
                    begin = mid
                    break
                else:
                    high = mid - 1

        # Binary Search for End
        low = 0
        high = len(nums) - 1
        while low <= high:

            mid = int((high + low)/2)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid == len(nums) - 1:
                    end = len(nums) - 1
                    break
                elif nums[mid + 1] > target:
                    end = mid
                    break
                else:
                    low = mid + 1

        return [begin, end]
