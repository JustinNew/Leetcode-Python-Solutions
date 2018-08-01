# 78. Subsets

class Solution(object):

    # Iteratively insert new elements in the existing list to create new list

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]

        result = [[]]
        for i in nums:
            temp = []
            for l in result:
                temp.append(l + [i])
            result += temp

        return result

    # Recursively choose to include first or not, second or not, ...

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]

        result = []
        n = len(nums)

        def util(i, temp):
            if i == n:
                result.append(temp)
                return

            util(i + 1, temp + [nums[i]])
            util(i + 1, temp)

            return 

        util(0, [])

        return result

# 90. Subsets II

# With duplicates

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]

        result = [[]]
        nums.sort()

        prev = None
        for i in nums:
            if i != prev:
                temp = []
                for l in result:
                    temp.append(l + [i])
                result += temp
                prev = i
            else:
                t = []
                for l in temp:
                    t.append(l + [i])
                result += t
                temp = t

        return result

    # Recursively choose first or not, second or not, ...
    # Add additional prev and flag to deal with duplicates.

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]

        result = []
        nums.sort()
        n = len(nums)

        def util(i, prev, temp, flag):
            if i == n:
                result.append(temp)
                return

            if nums[i] != prev:
                util(i + 1, nums[i], temp + [nums[i]], 1)
                util(i + 1, nums[i], temp, 0)
            else:
                if flag == 1:
                    util(i + 1, nums[i], temp + [nums[i]], 1)
                    util(i + 1, nums[i], temp, 0)
                else:
                    util(i + 1, nums[i], temp, 0)

            return

        util(0, None, [], 0)

        return result
