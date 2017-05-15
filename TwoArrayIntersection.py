class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        res = []

        i =0
        j = 0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i += 1
            elif nums1[i]>nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res


    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        c = Counter(nums2)
        res = []

        for i in nums1:
            j = c.get(i, 0)
            if j>0:
                res.append(i)
                c = c - Counter([i])

        return res
