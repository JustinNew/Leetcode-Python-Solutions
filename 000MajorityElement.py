# 169. Majority Element

# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
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

#######################################################################################################
# 169. Majority Element

class Solution:
    #
    # Boyer–Moore majority vote algorithm
    #

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cur = float('inf')

        for i in nums:
            if cur == i:
                count += 1
            else:
                if count == 0:
                    cur = i
                    count += 1
                else:
                    count -= 1

        return cur

#######################################################################################################
# Exactly the same idea as 169.
# 229. Majority Element II

# Boyer-Moore Majority Vote algorithm
# https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        cur1 = float('inf')
        cur2 = float('inf')
        count1 = 0
        count2 = 0

        for i in nums:
            if cur1 == i:
                count1 += 1
            elif cur2 == i:
                count2 += 1
            else:
                if count1 == 0:
                    cur1 = i
                    count1 += 1
                elif count2 == 0:
                    cur2 = i
                    count2 += 1
                else:
                    count1 -= 1
                    count2 -= 1

        l = len(nums)
        count1 = 0
        count2 = 0
        for i in nums:
            if i == cur1:
                count1 += 1
            elif i == cur2:
                count2 += 1
        res = []
        if count1 > int(l / 3):
            res.append(cur1)
        if count2 > int(l / 3):
            res.append(cur2)

        return res
