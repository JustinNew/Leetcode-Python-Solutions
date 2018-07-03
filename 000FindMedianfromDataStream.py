# 295. Find Median from Data Stream

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = {}

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if num in self.d:
            self.d[num] += 1
        else:
            self.d[num] = 1

        return


    def findMedian(self):
        """
        :rtype: float
        """
        l = [(k,v) for k, v in self.d.items()]
        l.sort(key=lambda x: x[0])
        count = sum([i[1] for i in l])
        
        if count % 2 == 0:
            m1 = int(count / 2)
            m2 = m1 - 1
            return (self.find(l, m1) + self.find(l, m2)) / 2
        else:
            m = int(count / 2)
            return self.find(l, m)

    def find(self, l, m):
 
        count = 0
        for i in l:
            count += i[1]
            if count >= m + 1:
                return i[0]
            
        return None


# Using two heap.

class MedianFinder:
    import heapq
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = [] # store the small half, top is the largest in the small part
        self.large = [] # store the large half, top is the smallest in the large part

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        if num <= -self.small[0]:
            # push to small part
            heapq.heappush(self.small, -num)
        else:
            # push to large part
            heapq.heappush(self.large, num)
        # adjust small and large balance
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2.0
        return -float(self.small[0]) if len(self.small) > len(self.large) else float(self.large[0])
