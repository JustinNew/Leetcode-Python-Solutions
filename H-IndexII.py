# 275. H-Index II

class Solution:
    def hIndex1(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        hindex = 0
        l = len(citations)
        for i in range(l - 1, -1, -1):
            t_min = min(citations[i], l - i)
            if t_min > hindex:
                hindex = t_min

        return hindex

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        hindex = 0
        l = len(citations)
        low = 0
        high = l - 1
        while low <= high:
            mid = int((low + high) / 2)
            if l - mid <= citations[mid]:
                if mid - 1 >= 0 and l - mid + 1 > citations[mid - 1]:
                    return l - mid
                elif mid == 0:
                    return l
                else:
                    high = mid - 1
            elif l - mid > citations[mid]:
                low = mid + 1 

        if l == 0:
            return 0
        elif low > high:
            return citations[-1]

if __name__ == '__main__':

    so = Solution()
    print(so.hIndex([0,1,3,5,5,5,6]))
