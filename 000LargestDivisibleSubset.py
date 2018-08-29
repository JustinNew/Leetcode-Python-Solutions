# 368. Largest Divisible Subset

'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
----------

We first do some math work. For two numbers, A and B, if A < B, A % B must > 0 (A != 0). The only chance A % B == 0 must be A >= B.

With this idea, we sort the list. Then, the question turns similar to no.300 longest increasing subsequence. For ith number, its largest divisible subset is the max of subset of any j from 0 - i-1 in which nums[i] % nums[j] == 0.
'''

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        from copy import copy
        nums.sort()
        n = len(nums)
        if n == 0: return []
        dp = [0] * n
        dp[0] = [nums[0]]
        
        for i in xrange(1, n):
            curNum = nums[i]
            maxSet = []
            for j in xrange(i):
                if curNum % nums[j] == 0:
                    localSet = copy(dp[j])
                    if len(localSet) > len(maxSet):
                        maxSet = localSet
            
            maxSet.append(nums[i])
            dp[i] = maxSet
        
        res = []
        for localSet in dp:
            if len(localSet) > len(res):
                res = localSet
        return res 
