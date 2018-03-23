# 57. Insert Interval

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        result = []
        times = []
        for i in intervals + [newInterval]:

            times.append((i.start, 1))
            times.append((i.end, -1))

        times.sort(key = lambda x: (x[0], -1*x[1]))

        flag = 0

        for i in range(len(times)):

            (t, value) = times[i]
            if value == 1 and flag == 0: 
                start = t
            elif value == -1 and flag + value == 0:
                result.append([start, t])
            flag += value

        return result
