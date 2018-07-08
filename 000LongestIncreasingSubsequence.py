# 300. Longest Increasing Subsequence

class Solution:

    # My solution.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        # To avoid Time Limit Exceeded.
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                flag = 1
        if flag == 0:
            return len(nums)

        result = {}
        result[1] = [nums[0]]

        for i in range(1, len(nums)):
            temp = {k:v for (k, v) in result.items()}
            for lgth in result:
                if nums[i] < result[1][0]:
                    temp[1] = [nums[i]]
                elif nums[i] > result[lgth][-1]:
                    if lgth + 1 in result and nums[i] < result[lgth + 1][-1]:
                        temp[lgth + 1] = result[lgth] + [nums[i]]
                    elif lgth + 1 not in result:
                        temp[lgth + 1] = result[lgth] + [nums[i]]

            result = temp

        return max(result.keys())

    # Dynamic Programming.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        lis = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1

        return max(lis)

'''
tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6

We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:

(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]
Doing so will maintain the tails invariant. The the final answer is just the size.
'''
def lengthOfLIS(self, nums):
    def search(temp, left, right, target):
        if left == right:
            return left
        mid = left+(right-left)/2
        return search(temp, mid+1, right, target) if temp[mid]<target else search(temp, left, mid, target)
    temp = []
    for num in nums:
        pos = search(temp, 0, len(temp), num)
        if pos >=len(temp):
            temp.append(num)
        else:
            temp[pos]=num
    return len(temp)
