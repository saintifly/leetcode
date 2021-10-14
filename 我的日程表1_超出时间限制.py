class MyCalendar(object):

    def __init__(self):
        self.book_time_his = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.book_time_his ==[]:
            self.book_time_his.append([start,end])
            return True
        for i in self.book_time_his:
            if start>=i[0] and end <=i[1]:
                return False
            if start <i[0] and end > i[0]:
                return False
            if start <i[1] and end >= i[1]:
                return False
        print(self.book_time_his)
        self.book_time_his.append([start,end])
        return True




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)