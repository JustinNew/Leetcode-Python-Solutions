class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        l = len(nums)
        k = k % l
        while k > 0:
            temp = nums[l-1]
            for i in range(l-1):
                nums[l-1-i] = nums[l-i-2]
            nums[0] = temp
            k -= 1
            print(k)

        return
               

    def rotate1(self, nums, k):

        k = k % len(nums)
        i = 0
        j = len(nums) - 1 - k 

        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i = len(nums) - k
        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i = 0 
        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return
        


if __name__=='__main__':

    a = [1,2,3,4,5,6,7]
    so = Solution()

    so.rotate1(a, 10) 

    print(a)
