# 179. Largest Number

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(nums).lstrip('0') or '0'
