# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.l = []
        while iterator.hasNext():
            self.l.append(iterator.next())
        self.l = self.l[::-1]

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.l) > 0:
            return self.l[-1]
        else:
            return

    def next(self):
        """
        :rtype: int
        """
        return self.l.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.l) > 0:
            return True
        else:
            return False

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class PeekingIterator(object):
    def __init__(self, iterator):
        self.i = iterator
        self.n = None

    def peek(self):
        if not self.n:
            self.n = self.i.next()
        return self.n

    def next(self):
        if not self.n:
            self.n = self.i.next()
        a = self.n
        self.n = None
        return a

    def hasNext(self):
        if self.n:
            return True
        return self.i.hasNext()
