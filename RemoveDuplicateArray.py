class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return len(nums)

        fill = 0
        index = 1

        while index < len(nums):

            if nums[index] != nums[fill]:
                fill += 1
                nums[fill] = nums[index]

            index += 1

        print (nums[:fill+1])

        return fill+1

if __name__=='__main__':

    a = [1,1,2,2,3,3,3]
    so = Solution()
    print (so.removeDuplicates(a))
