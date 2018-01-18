# Leetcode 729
# My Calendar I

class MyCalendar:

    def __init__(self):

            self.books = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if len(self.books) == 0:
            self.books.append([start, end])
            return True
        else:
            if end <= self.books[0][0]:
                self.books.insert(0, [start, end])
                return True
            else:
                for i in range(0, len(self.books)-1):
                    if start <= self.books[i][0] and end > self.books[i][0]:
                        return False
                    elif start > self.books[i][0] and start < self.books[i][1]:
                        return False
                    elif start >= self.books[i][1] and end <= self.books[i+1][0]:
                        self.books.insert(i+1, [start, end])
                        return True
                            
                if end <= self.books[-1][0]:
                    self.books.insert(len(self.books)-2,[start, end])
                    return True
                elif start >= self.books[-1][1]:
                    self.books.append([start, end])
                    return True
                else:
                    return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


### Exceeded time limit
class MyCalendar:

    def __init__(self):

        self.books = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if len(self.books) == 0:
            self.books.append([start, end])
            return True
        else:
            self.books.sort(key = lambda x: x[0])

            if end <= self.books[0][0]:
                self.books.append([start, end])
                return True
            elif start >= self.books[-1][1]:
                self.books.append([start, end])
                return True
            else:
                for i in range(0, len(self.books)):
                    if start <= self.books[i][0] and end > self.books[i][0]:
                        return False
                    elif start > self.books[i][0] and start < self.books[i][1]:
                        return False

                self.books.append([start, end])
                return True