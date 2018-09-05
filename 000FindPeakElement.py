# 162. Find Peak Element

'''
Basic Idea: Binary search

Elaboration: 
 if an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right, because the elements on its right is either 
   1. always increasing  -> the right-most element is the peak
   2. always decreasing  -> the left-most element is the peak
   3. first increasing then decreasing -> the pivot point is the peak
   4. first decreasing then increasing -> the left-most element is the peak  

   Therefore, we can find the peak only on its right elements(cut the array to half)

   The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.

Conditions:
     1. array length is 1  -> return the only index 
     2. array length is 2  -> return the bigger number's index 
     3. array length is bigger than 2 -> 
           (1) find mid, compare it with its left and right neighbors  
           (2) return mid if nums[mid] greater than both neighbors
           (3) take the right half array if nums[mid] smaller than right neighbor
           (4) otherwise, take the left half

Run time: O(logn)
Memory: constant
Test cases: 
     [1]
     [1,2]
     [2,1]
     [1,2,3]
     [3,2,1]
     [2,1,3]
'''

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums)-1

        # handle condition 3
        while left < right-1:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
            
        # handle condition 1 and 2
        return left if nums[left] >= nums[right] else right

    # My solution
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        h = len(nums) - 1
        
        if h == 1:
            return 0 if nums[0] > nums[1] else 1

        while l < h:

            mid = int((l + h) / 2)
            if mid - 1 < 0 or mid + 1 > len(nums) - 1:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                h = mid    # Pay attention to this, h = mid instead of h = mid - 1

        return l
