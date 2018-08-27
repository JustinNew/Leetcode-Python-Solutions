# 4. Median of Two Sorted Arrays
# Explanation with figure:
# https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/ 

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l = len(nums1) + len(nums2)

        # when k is bigger than the sum of a and b's median indices
        # Pay special attention to ia + ib == k, can run a simple test with [1,2], [3].
        # Smaller first to avoid complication.
        #####################################
        # Remember kth is '0' based.        #
        # Remember it's m1 + 1.             #
        #####################################
        def kth(list1, list2, k):

            if not list1:
                return list2[k]
            if not list2:
                return list1[k]

            m1 = int(len(list1) / 2)
            m2 = int(len(list2) / 2)

            if m1 + m2 < k:
                # if list2's median is bigger than list1's, list1's first half doesn't include k
                if list1[m1] < list2[m2]:
                    return kth(list1[m1 + 1:], list2, k - m1 - 1)
                else:
                    return kth(list1, list2[m2 + 1:], k - m2 - 1)

            # when k is smaller than the sum of a and b's median indices
            else:
                if list1[m1] < list2[m2]:
                    return kth(list1, list2[:m2], k)
                else:
                    return kth(list1[:m1], list2, k)

        if l % 2 == 0:
            return (kth(nums1, nums2, int(l / 2)) + kth(nums1, nums2, int(l / 2) - 1)) / 2
        else:
            return kth(nums1, nums2, int(l / 2))
