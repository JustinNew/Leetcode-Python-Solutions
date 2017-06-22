# Given a list of meeting times, checks if any of them overlaps. 
# The follow-up question is to return the minimum number of rooms required to accommodate all the meetings.
# [(1, 4), (5, 6), (8, 9), (2, 6)]

# Sort the start and end points.
# Go through the sorted list
# When encounter 'start' RoomNumber increase by on.
# When encounter 'end'

def GetRoomNumber(nums):

        """
        :type nums: List[(int,int)]
        :rtype: int
        """

        times = []
        for i in range(len(nums)):
            (start, end) = nums[i]
            times.append((start, 1))
            times.append((end, -1))

        times.sort(key=lambda x:x[0])

        result = 0
        room = 0
        for i in range(len(times)):
            (time, flag) = times[i]
            room += flag
            result = max(result, room)

        return result

a = [(1, 4), (5, 6), (8, 9), (2, 6)]

print (GetRoomNumber(a))
