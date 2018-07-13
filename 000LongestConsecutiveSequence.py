# 128. Longest Consecutive Sequence

# Time O(n), so can not sort.
# Use dictionary.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)

        d = {}
        for i in nums:
            if i in d:
                continue
            elif i + 1 in d and i - 1 in d:
                d[i] = 1 + d[i + 1] + d[i - 1]
                right = i + 1
                while right in d:
                    d[right] = d[i]
                    right += 1
                left = i - 1
                while left in d:
                    d[left] = d[i]
                    left -= 1
            elif i + 1 in d:
                d[i] = 1 + d[i + 1]
                right = i + 1
                while right in d:
                    d[right] = d[i]
                    right += 1
            elif i - 1 in d:
                d[i] = 1 + d[i - 1]
                left = i - 1
                while left in d:
                    d[left] = d[i]
                    left -= 1
            elif i not in d:
                d[i] = 1

        return max([v for v in d.values()])

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
