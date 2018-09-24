# 128. Longest Consecutive Sequence

# Time O(n), so can not sort.
# Use dictionary
# Only need to update boundary
# 4 cases
# For every i need to have a record in dictionary

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        d = {}
        for i in nums:
            if i in d.keys():
                continue
            elif i - 1 in d.keys() and i + 1 in d.keys():
                left = i - d[i - 1]
                right = i + d[i + 1]
                d[left], d[right] = d[i - 1] + 1 + d[i + 1], d[i - 1] + 1 + d[i + 1]
                d[i] = d[left]
            elif i - 1 in d.keys():
                left = i - d[i - 1]
                d[i], d[left] = 1 + d[i - 1], 1 + d[i - 1]
            elif i + 1 in d.keys():
                right = i + d[i + 1]
                d[i], d[right] = 1 + d[i + 1], 1 + d[i + 1]
            else:
                d[i] = 1

        return max(d.values())

    ####################################################################################################################
    # Improve it.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)

        d = {}
        res = 0
        for i in nums:
            if i not in d:
                left = d.get(i - 1, 0)
                right = d.get(i + 1, 0)
                m = 1 + left + right
                d[i] = m
                res = max(res, m)

                d[i - left] = m
                d[i + right] = m
            else:
                continue

        return res

    ###################################################################################################################
    # Sort first.
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        m = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                if cur > m:
                    m = cur
            elif nums[i] == nums[i-1]:
                continue
            else:
                cur = 1
                
        return m
