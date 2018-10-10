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

    ###############################################################################################################
    # My solution, customized merge sort.
    # If x + y > y + x, then x first followed by y.

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def mySort(arr):

            if len(arr) <= 1:
                return arr

            l = len(arr)
            mid = int(l / 2)

            # Divide
            left = mySort(arr[:mid])
            right = mySort(arr[mid:])

            # Merge
            p1 = 0
            p2 = 0
            res = []

            while p1 < len(left) and p2 < len(right):
                if int(str(left[p1]) + str(right[p2])) > int(str(right[p2]) + str(left[p1])):
                    res.append(left[p1])
                    p1 += 1
                else:
                    res.append(right[p2])
                    p2 += 1

            if p1 < len(left):
                res += left[p1:]
            if p2 < len(right):
                res += right[p2:]

            return res

        nums = mySort(nums)
        r = ''
        for i in nums:
            r += str(i)

        return str(int(r))
