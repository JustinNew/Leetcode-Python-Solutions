# 75. Sort Colors

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            elif nums[i] == 2:
                count2 += 1
                
        i = 0
        while i < len(nums) and count0 > 0:
            nums[i] = 0
            i += 1
            count0 -= 1
            
        while i < len(nums) and count1 > 0:
            nums[i] = 1
            i += 1
            count1 -= 1
            
        while i < len(nums) and count2 > 0:
            nums[i] = 2
            i += 1
            count2 -= 1
            
        return

    '''
    Requirement: one pass, inplace
    The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.
    '''

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        if l <= 1:
            return

        p0 = 0
        p2 = l - 1
        for i in range(l):
            while nums[i] == 2 and i < p2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            while nums[i] == 0 and i > p0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

        return 
