class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.sm = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.s1) == 0:
            self.sm.append(x)
        else:
            if x <= self.sm[-1]:
                self.sm.append(x)
        self.s1.append(x)

        return

    def pop(self):
        """
        :rtype: void
        """
        if len(self.s1) != 0:
            temp = self.s1.pop()
            if temp == self.sm[-1]:
                self.sm.pop()
        return
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.s1) == 0:
            print ('Stack is empty.')
            return
        else:
            return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.sm[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
