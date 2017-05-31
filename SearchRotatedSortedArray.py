class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = int((i + j) / 2)
            if nums[mid] > nums[j]:
                i = mid + 1 
            else:
                j = mid
        pivot = i
        
        flag = 0
        if pivot == 0:
            start = 0
            end = len(nums) -1
            flag = 1
        elif nums[pivot] <= target and nums[-1] >= target:
            start = pivot
            end =len(nums) - 1
            flag = 1
        elif nums[0] <= target and nums[pivot-1] >= target:
            start = 0
            end = pivot - 1
            flag = 1
        
        if flag == 1:
            while start <= end:
                mid = int((start+end)/2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        
        return -1

if __name__=='__main__': 

    so = Solution()
    a = [3,5,1]
    print (so.search(a, 3))
