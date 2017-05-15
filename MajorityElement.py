class Solution(object):
    #
    # Boyer–Moore majority vote algorithm
    #
    def majorityElement_moore(self, nums):
        majority_num = 0
        count = 0
        for num in nums:
            if count == 0:
                majority_num = num
            if majority_num != num:
                count -= 1
            else:
                count += 1
        return majority_num

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        for i in set(nums):
            if nums.count(i) > l/2.0:
                return i

        return -1

    def majorityElement(self, nums):

        from collections import Counter
        c = Counter(nums)
        l = len(nums)
        for i in c.keys():
            if c.get(i, 0) > l/2.0:
                return i

    def majorityElement(self, nums):

        nums = sorted(nums)
        return nums[len(nums)/2]
