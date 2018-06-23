# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        d = [(k, v) for k, v in d.items()]
        d.sort(key=lambda a: -1 * a[1])

        result = []

        for i in range(k):
            result.append(d[i][0])

        return result
