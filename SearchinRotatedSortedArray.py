# 33. Search in Rotated Sorted Array
# First find the rotated min point, then search in the two rotated array.

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) != 0:
            pivot = self.pivotPoint(nums)
        else:
            return -1

        if pivot == 0:
            return self.binarySearch(nums, 0, len(nums) - 1, target)
        elif target >= nums[0] and target <= nums[pivot - 1]:
            return self.binarySearch(nums, 0, pivot - 1, target)
        else:
            return self.binarySearch(nums, pivot, len(nums) - 1, target)

    def pivotPoint(self, nums):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return mid

    def binarySearch(self, nums, left, right, target):

            while left <= right:
                mid = int((left + right) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

if __name__ == '__main__':

    s = Solution()
    print (s.search([0,1,2,3,4,5,6], 3))
