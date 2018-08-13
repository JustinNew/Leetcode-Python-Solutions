# 55. Jump Game

class Solution(object):
    ###########################################################################
    # Intuition
    # Start from first and go one by one to calculate the reachable state 
    # Time Limit Exceeded
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(len(nums) - 1):
            if dp[i] == 0:
                return False
            else:
                for j in range(nums[i]):
                    if i + j + 1 < len(nums):
                        dp[i + j + 1] = 1

        return True if dp[-1] == 1 else False

    ####################################################################
    # Improve on the first approach
    # For every step, calculate the max reachable state
    # Time Limit Exceeded
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        maxReach = 0
        for i in range(len(nums) - 1):
            if dp[i] == 1:
                maxReach = i + nums[i]
                if maxReach >= len(nums):
                    return True
                for j in range(i + 1, maxReach + 1):
                    dp[j] = 1
            else:
                return False

        return True if dp[-1] == 1 else False

    ####################################################################
    # O(n)
    # Greedy, every time calculate the max reachable
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        maxReach = 0
        i = 0
        while 1:
            t_m = maxReach
            for j in range(i, maxReach + 1):
                t_m = max(t_m, j + nums[j])
            if t_m == maxReach:
                return False
            if t_m >= len(nums) - 1:
                return True
            maxReach = t_m
            i = j + 1

#############################################################################################
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
