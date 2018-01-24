# 55. Jump Game

# This can be used by DP.
# Pay attention to "return self.util(nums, i+j+1, nums[i+j+1])"
# Need to return on the self recursion call.


# But actually it can be easily solved without DP.
# Trick: using max_reach = max(max_reach, i+x)


def canJump(self, nums):
    max_reach, n = 0, len(nums)
    for i, x in enumerate(nums):
        if max_reach < i: return False
        if max_reach >= n - 1: return True
        max_reach = max(max_reach, i + x)


############################################################################################# 
# Another one. 
#############################################################################################
def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

#############################################################################################
# My DP does not work (RecursionError: maximum recursion depth exceeded in comparison)
############################################################################################# 
class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) <= 0:
            return True

        return self.util(nums, 0, nums[0])

    def util(self, nums, i, length):

        if (i + length) >= (len(nums) - 1):
            return True
        elif length == 0:
            return False
        else:
            for j in range(length):
                return self.util(nums, i+j+1, nums[i+j+1])

if __name__ == '__main__':

    s = Solution()
    print (s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))
