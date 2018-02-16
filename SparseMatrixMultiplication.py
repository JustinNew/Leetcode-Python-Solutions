# 311. Sparse Matrix Multiplication

class Solution(object):

    # Time limit exceeded.
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        r_a = len(A)
        c_a = len(A[0])

        r_b = len(B)
        c_b = len(B[0])

        result = [[0 for j in range(c_b)] for i in range(r_a)]

        for i in range(r_a):

            for j in range(c_b):
                temp = 0

                for k in range(c_a):
                    temp += A[i][k] * B[k][j]

                result[i][j] = temp

        return result

    # Just do multiply for non-zero rows in A and non-zero columns in B.
    def multiply2(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        r_a = len(A)
        c_a = len(A[0])

        r_b = len(B)
        c_b = len(B[0])

        result = [[0 for j in range(c_b)] for i in range(r_a)]

        r_list = []
        for i in range(r_a):
            flag = 0
            for j in range(c_a):
                if A[i][j] != 0:
                    flag = 1
                    break
            if flag == 1:
                r_list.append(i)

        c_list = []
        for i in range(c_b):
            flag = 0
            for j in range(r_b):
                if B[j][i] != 0:
                    flag = 1
                    break
            if flag == 1:
                c_list.append(i)

        for i in r_list:
            for j in c_list:
                temp = 0
                for k in range(c_a):
                    temp += A[i][k] * B[k][j]
                result[i][j] = temp

        return result
