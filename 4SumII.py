# 454. 4Sum II

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        A.sort()
        B.sort()
        C.sort()
        D.sort()

        if len(A) == 0:
            return 0

        result = 0
        for i in A:
            for j in B:
                s = -1 * i - j
                l = 0
                k = len(A) - 1
                while l < len(A) and k >= 0:
                    if C[l] + D[k] < s:
                        l += 1
                    elif C[l] + D[k] > s:
                        k -= 1
                    else:
                        c_1 = 1
                        while l + 1 < len(A) and C[l + 1] == C[l]:
                            c_1 += 1
                            l += 1
                        c_2 = 1
                        while k - 1 >= 0 and D[k - 1] == D[k]:
                            c_2 += 1
                            k -= 1
                        result += c_1 * c_2
                        l += 1

        return result

    # Use dictionary
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        sum_AB = {}
        for i in A:
            for j in B:
                sum_AB[i + j] = sum_AB.get(i + j, 0) + 1

        result = 0
        for i in C:
            for j in D:
                t = -1 * i - j
                result += sum_AB.get(t, 0)

        return result
