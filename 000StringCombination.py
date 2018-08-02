# 77. Combinations

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        if k > n:
            return []
        if k == n:
            return [[i + 1 for i in range(n)]]

        result = []
        def util(ndx, have, temp):
            if have == k:
                result.append(temp)
                return 
            elif ndx > n:
                return 
            elif n - ndx + 1 < k - have:
                return 
            else:
                for i in range(ndx, n + 1):
                    util(i + 1, have + 1, temp + [i])

                return 

        util(1, 0, [])
        return result

######################################################################
# Using Recursive Method.
# n, number of characters
# r, number of characters to pick
# idx, index of pick from n characters
# k, number of characters picked

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        import operator
        import functools

        times = []
        arr = [1,2,4,8,16,32,100,200,400,800]
        if num==0:
            times.append(str('0:00'))
            return times
        else:
            result = self.StringCombination(arr, num)

        for i in result:
            sum = functools.reduce(operator.add, i)
            hour = int(sum/100)
            min = sum%100
            if hour>11 or min>59:
                next
            elif min<10:
                times.append(str(hour)+':0'+str(min))
            else:
                times.append(str(hour)+':'+str(min))
        return times
