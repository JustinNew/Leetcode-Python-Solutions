# 278. First Bad Version
# Facebook Tag
# Binary Search


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        low = 1
        high = n

        while low <= high:

            mid = int((low + high)/2)

            if isBadVersion(mid) and mid == 1:
                return 1
            elif isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):
                high = mid - 1
            elif not isBadVersion(mid):
                low = mid + 1

        return -1

