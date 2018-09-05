# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        def findPivot(arr):

            l = 0
            h = len(arr) - 1

            while l < h:
                mid = int((l + h) / 2)
                if arr[mid] > arr[h]:
                    l = mid + 1
                else:
                    h = mid

            return l

        def search(low, high, val):

            if nums[low] > val or nums[high] < val:
                return -1

            l = low
            h = high
            while l <= h:
                mid = int((l + h) / 2)
                if nums[mid] == val:
                    return mid
                elif nums[mid] < val:
                    l = mid + 1
                else:
                    h = mid - 1

            return -1

        m = findPivot(nums)
        left = search(0, m - 1, target)
        right = search(m, len(nums) - 1, target)

        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1 
