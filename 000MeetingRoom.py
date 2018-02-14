# 253. Meeting Rooms II
# Facebook Tag

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        times = []
        for i in range(len(intervals)):

            (start, end) = (intervals[i].start, intervals[i].end)
            times.append((start, 1))
            times.append((end, -1))

        times.sort(key=lambda x: (x[0],x[1]))

        maxRoom = 0
        curRoom = 0

        for i in range(len(times)):

            curRoom += times[i][1]
            maxRoom = max(maxRoom, curRoom)

        return maxRoom
