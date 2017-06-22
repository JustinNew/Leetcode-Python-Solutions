class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if len(nums) == 0:
            return [-1,-1]
        if nums[0] > target or nums[-1] < target:
            return [-1,-1]
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + int((high - low)/2)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                if mid == 0 or nums[mid - 1] < target:
                    result.append(mid)
                    break
                else:
                    high = mid - 1
                
        low = 0
        high = len(nums) - 1        
        while low <= high:
            mid = low + int((high - low)/2)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    result.append(mid)
                    break
                else:
                    low = mid + 1
                    
        if len(result) == 0: 
            return [-1,-1]
        else:
            return result
