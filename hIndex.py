# 274. H-Index

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if len(citations) == 0:
            return 0

        citations.sort(reverse=True)

        for i in range(len(citations)):

            if citations[i] < i + 1:
                return min(i, citations[i-1])

        return (len(citations))
