# 352. Data Stream as Disjoint Intervals

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if len(self.s) == 0:
            self.s.append(Interval(val, val))
            return
        else:
            if val < self.s[0].start - 1:
                self.s.insert(0, Interval(val, val))
                return
            elif val == self.s[0].start - 1:
                self.s[0].start = val
                return
            elif val > self.s[-1].end + 1:
                self.s.append(Interval(val, val))
                return
            elif val == self.s[-1].end + 1:
                self.s[-1].end = val
                return
            else:
                for i in range(len(self.s) - 1):
                    if val == self.s[i].end + 1 and val == self.s[i + 1].start - 1:
                        self.s[i].end = self.s[i + 1].end
                        self.s.remove(self.s[i + 1])
                        return
                    elif val == self.s[i].end + 1:
                        self.s[i].end = val
                        return
                    elif val == self.s[i + 1].start - 1:
                        self.s[i + 1].start = val
                        return
                    elif val > self.s[i].end + 1 and val < self.s[i + 1].start - 1:
                        self.s.insert(i + 1, Interval(val, val))
                        return

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.s
        

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
