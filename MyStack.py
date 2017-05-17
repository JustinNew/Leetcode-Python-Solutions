class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if not self.q1:
            self.q2.append(x)
        elif not self.q2:
            self.q1.append(x)
        return 

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.q1:
            while len(self.q2) > 1:
                temp = self.q2.pop(0)
                self.q1.append(temp)
            result = self.q2.pop(0)
        elif not self.q2:
            while len(self.q1) > 1:
                temp = self.q1.pop(0)
                self.q2.append(temp)
            result = self.q1.pop(0)
        return result

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        result = self.pop()
        self.push(result)
        return result       

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        l = len(self.q1) + len(self.q2)
        return True if l == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty() 
