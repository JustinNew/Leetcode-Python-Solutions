# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.


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


# 229. Majority Element II
# Boyer-Moore Majority Vote algorithm 
# https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

class Solution:

    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):

        if not nums:
            return []

        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1 # Note: both need to subtract 1

        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]
