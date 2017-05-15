class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        from collections import Counter
        c = Counter(nums)
        for i in set(nums):
            if c.get(i, 0)>1:
                return True

        return False

    def containsDuplicate(self, nums):

        return len(nums) > len(set(nums)) 
