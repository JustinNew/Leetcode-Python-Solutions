# 398. Random Pick Index
# Using Reservoir Sampling K = 1. 

import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index, count = -1, 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) == 0: index = i
                count += 1
                
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)```
