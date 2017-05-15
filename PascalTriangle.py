class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        from collections import deque

        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        result = [[1],[1,1]]

        dq = deque()
        dq.append(1)
        dq.append(1)

        for i in range(numRows-2):
            t_l = [1]
            t_o = dq.popleft()
            while dq:
                t_n = dq.popleft()
                t_l.append(t_o+t_n)
                t_o = t_n
            t_l.append(1)
            result.append(t_l)
            for i in t_l:
                dq.append(i)

        return result

if __name__=='__main__':

    so = Solution()

    print (so.generate(6))
