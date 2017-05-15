class Solution():

    def MoveZeroes(self, nums):

        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j] = nums[i]
                j += 1
        
        while j < len(nums):
            nums[j] = 0
            j += 1

        return

if __name__=='__main__':

    l = [1,0,2,3,0,4,5]

    print 'Before move: ', l
    s = Solution()

    s.MoveZeroes(l)

    print 'After move: ', l
