# 46. Permutations

########################################################
# Pay attention to the different between the two.
########################################################
# If using result.append(), can not pass nums directly.
# There is problem about assignment.
# Create another list variable "temp".
# There is not problem if using print(). 

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []

        l = len(nums)
        result = []
        temp = []

        self.util(0, l, nums, result)

        return result

    def util(self, i, l, nums, result):

        if i == l:
            result.append(nums)
            return

        for j in range(i, l):
            nums[i], nums[j] = nums[j], nums[i]
            temp = [k for k in nums]
            self.util(i+1, l, temp, result)

        return

class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []

        l = len(nums)

        self.util(0, l, nums)

        return

    def util(self, i, l, nums):

        if i == l:
            print(nums)
            return

        for j in range(i, l):
            nums[i], nums[j] = nums[j], nums[i]
            self.util(i+1, l, nums)
            nums[i], nums[j] = nums[j], nums[i]

        return

########################################################
# Excellent solution.
# Without recursion
# The basic idea is, to permute n numbers, we can add the nth number into 
# the resulting List<List<Integer>> from the n-1 numbers, in every possible position.
# 1. [[1]]
# 2. [[2,1], [1,2]]
# 3. [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2],[1,2,3]]
#

def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms

if __name__ == '__main__':

    s = Solution()
    s2 = Solution2()
    print (s.permute([1,2,3]))
    s2.permute([1,2,3])
