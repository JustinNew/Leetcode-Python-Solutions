# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            element = nums[i]
            if element < 0:
                element *= -1
            if nums[element - 1] > 0:
                nums[element - 1] *= -1
            else:
                result.append(element)
            
        return result
