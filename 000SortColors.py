# 75. Sort Colors

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 2
        
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
