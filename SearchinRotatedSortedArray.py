# 33. Search in Rotated Sorted Array

# Facebook Tag

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def findPivot(arr):
            l = len(arr)
            if l == 1:
                return 0

            low = 0
            high = l - 1
            while low < high:
                mid = int((low + high) / 2)
                if arr[mid] > arr[high]:
                    low = mid + 1
                else:
                    high = mid

            return low

        def findTarget(low, high):

            while low <= high:
                mid = int((low + high) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return -1

        p = findPivot(nums)
        i1 = findTarget(0, p - 1)
        i2 = findTarget(p, len(nums) - 1)

        if i1 != -1:
            return i1
        elif i2 != -1:
            return i2
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = len(nums)
        if l == 0:
            return -1

        low = 0
        high = l - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            else:
                # Pivot on the right
                if nums[mid] > nums[high]:
                    if nums[low] <= target and target <= nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                # Pivot on the left
                else:
                    if nums[mid] <= target and target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1

        return -1
