class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_list = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.num_list.append(x)


    def pop(self):
        """
        :rtype: None
        """
        self.num_list.pop(-1)


    def top(self):
        """
        :rtype: int
        """
        if self.num_list==[]:
            return None
        return self.num_list[-1]


    def getMin(self):
        """
        :rtype: int
        """
        min_val = sys.maxint
        for i in self.num_list:
            if i < min_val:
                min_val = i
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()