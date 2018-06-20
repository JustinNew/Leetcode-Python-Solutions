# 179. Largest Number

# If x + y > y + x, then x first followed by y. 

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):

        nums = [str(x) for x in nums]
        # Discarded in Python 3.x.
        # nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(lambda x, y: -1 if str(x) + str(y) > str(y) + str(x) else 1))
        return ''.join(nums).lstrip('0') or '0'
