# 45. Jump Game II

# Dynamic Programming

# [ 2, 3, 1, 1, 4 ]
#   0  0  0  0  0
#      1  1
#         2  2  2
#         1  2  2
#            2  2
#               3
#               2

# Greedy

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        steps = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(nums[i]):
                t = 1 + steps[i]
                if i + j + 1 < len(nums):
                    if steps[i + j + 1] != 0:
                        steps[i + j + 1] = min(t, steps[i + j + 1])
                    else:
                        steps[i + j + 1] = t

        return steps[-1]

    def jump2(self, A):
        last_max_reach, current_max_reach = 0 , 0
        njump , i = 0 , 0
        while current_max_reach < len(A)-1:
            while i <= last_max_reach:
                current_max_reach = max(i+A[i],current_max_reach)
                i+=1
            if last_max_reach == current_max_reach:
                return -1
            last_max_reach = current_max_reach
            njump+=1
        return njump
 
    ############################################################################
    # Greedy
    # Similar to 55 Jump Game
    # Every time, calculate the max reachable state.
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        maxReach = 0
        i = 0
        count = 0
        while 1:
            t_m = maxReach
            for j in range(i, maxReach + 1):
                t_m = max(t_m, j + nums[j])
            count += 1
            if t_m == maxReach:
                return False
            if t_m >= len(nums) - 1:
                return count
            maxReach = t_m
            i = j + 1
