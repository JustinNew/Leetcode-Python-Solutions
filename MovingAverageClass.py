# Calculate the moving average (with a fixed window size) of a data stream.
from collections import deque

class MovingAverage():

    def __init__(self,m):
        self.m = m
        self.q = deque()
        self.sum = 0.0

    def next(self,int):
        if len(self.q)<m:
            self.q.append(int)
            self.sum += int
            return self.sum/len(self.q)
        else:
            self.q.append(int)
            self.sum = self.sum + int - self.q.popleft()
            return self.sum/len(self.q)

if __name__=='__main__':

    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    m = 4

    solution = MovingAverage(4)
    for i in range(len(a)):
        print solution.next(a[i])
