# 153. Find Minimum in Rotated Sorted Array

# Binary search modification

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # One difference with binary search.
        while left < right:

            mid = int((left + right) / 2)

            # Just compare nums[mid] with the last element.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Another difference with binary search.
            else:
                right = mid

        return nums[left]

if __name__ == '__main__':

    so = Solution()
    print(so.findMin([3,4,5,1,2]))
