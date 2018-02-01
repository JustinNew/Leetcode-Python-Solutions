# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)

        n = len(nums)
        removed = 0
        duplicated = 0
        p1 = 0 

        for p2 in range(1, len(nums)):

            if nums[p2] != nums[p1]:
                p1 += 1
                nums[p1] = nums[p2]
                duplicated = 0
            elif nums[p2] == nums[p1]:
                if duplicated == 0:
                    p1 +=1
                    nums[p1] = nums[p2]
                    duplicated = 1
                else:
                    removed += 1

        return n - removed

if __name__ == '__main__':

    s = Solution()
    print (s.removeDuplicates([1,1,1,1,2,2,2,2,2,2,2,3]))
