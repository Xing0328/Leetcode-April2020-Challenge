class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min == []:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.min[-1]:
            
            self.stack.pop()
            self.min.pop()
        else:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()