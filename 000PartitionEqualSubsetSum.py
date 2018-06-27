# 416. Partition Equal Subset Sum

class Solution:

# 1. Get sum, sum % 2 == 0
# 2. Find subset that equal sum / 2.
# 3. Backtrack problem
# Sort reversely and add tricks to exit early, otherwise it will have "Time Limit Exceeded".

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return True

        s = sum(nums)

        if s % 2 != 0:
            return False

        s = int(s / 2)
        used = [0 for i in nums]
        nums.sort(reverse=True)

        if self.util(nums, s, 0, used):
            return True
        else:
            return False

    def util(self, nums, s, start, used):

        if s == 0:
            return True 
        if s < 0:
            return False
        if sum(nums[start:]) < s:
            return False

        for i in range(start, len(nums)):
            if used[i] == 0:
                used[i] = 1
                if self.util(nums, s - nums[i], i + 1, used):
                    return True
                used[i] = 0

        return False

'''
One trick is to do a early check if the maximum of nums is bigger than half of the sum, this can save some efforts for impossible cases. Also we can sort nums in decreasing order to check bigger element first.

Also, for memo, we only need current accumulative value curr not the index i. Because smaller i means we have more candidates to choose, if memo[curr] == False for previous smaller i, surely we know there is no answer for current bigger i.
'''
# Use memo = {} to reduce repeated calculation.

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, half = len(nums), sum(nums) >> 1
        if sum(nums) & 1 or max(nums) > half: return False
        nums.sort(reverse = True)
        memo = {}
        
        def dfs(curr, i):
            if curr >= half: return curr == half
            if curr not in memo:
                memo[curr] = any(dfs(curr + nums[j], j) for j in range(i+1, n))
            return memo[curr]
        
        return not nums or any(dfs(nums[i], i) for i in range(n))

# Dynamic Programming
# Build up a table from 0 to sum / 2.

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        s = sum(nums)
        if s % 2 != 0:
            return False
        s = int(s / 2)

        table = [False for i in range(s + 1)]
        table[0] = True

        # Need to be careful when update for each round.
        # temp list is required, can not directly update table list.
        nums.sort()
        for i in nums:
            temp = [i for i in table]
            for j in range(s+1):
                if table[j] and i + j <= s:
                    if i + j == s:
                        return True
                    temp[i + j] = True
            table = [i for i in temp]

        return table[-1]
