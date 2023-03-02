from bisect import bisect_right,bisect_left
class MyCalendar:

    def __init__(self):
        self.bookList  = [0,10**9]
        self.bookinfo =  []

    def book(self, start: int, end: int) -> bool:
        left_point = bisect_right(self.bookList,start)
        right_point = bisect_left(self.bookList,end)
        if left_point == right_point and end >start:
            if [self.bookList[left_point-1],self.bookList[left_point]] in self.bookinfo:
                return False
            else:
                self.bookinfo.append([start,end])
                # self.bookList = self.bookList[:left_point] + [start,end]+self.bookList[left_point:]
                self.bookList = sorted(list(set(self.bookList+[start,end])))
                return True
        else:
            return False

if __name__ == '__main__':
    calendar = MyCalendar()
    a = calendar.book(1,2)
    print(a)
    a = calendar.book(1,3)
    print(a)
    a = calendar.book(2,5)
    print(a)


