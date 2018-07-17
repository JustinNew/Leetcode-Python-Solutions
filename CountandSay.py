# 38. Count and Say

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'

        result = [1]

        for i in range(n - 1):

            temp = []
            prev = float('inf')
            count = 0
            for j in result:
                if prev == float('inf'):
                    count = 1
                    prev = j
                elif j == prev:
                    count += 1
                else:
                    t = []
                    while count > 0:
                        t.append(count % 10)
                        count = int(count / 10)
                    temp.extend(t[::-1])
                    temp.append(prev)
                    count = 1
                    prev = j
            temp.append(count)
            temp.append(prev)
            result = [k for k in temp]

        return ''.join([str(i) for i in result])
