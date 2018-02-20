# 56. Merge Intervals
# Facebook Tag

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = []
        for i in intervals:
            start, end = i.start, i.end
            l.append((start, 1))
            l.append((end, -1))
            
        r = []
        l.sort(key=lambda x: (x[0], -1*x[1]))
        flag = 0
        for i in l:
            (time, t) = (i[0], i[1])
            if flag == 0 and t == 1:
                start = time
            flag += t
            if flag == 0 and t == -1:
                end = time
                r.append([start, end])
                
        return r
