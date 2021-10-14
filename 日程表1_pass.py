class MyCalendar:

    def __init__(self):
        # from sortedcontainers import SortedSet as SS
        # self.date = SS()
        from sortedcontainers import SortedList
        self.date = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.date.bisect_right(start)
        if idx == len(self.date) or idx%2==0 and self.date[idx] >= end:
            self.date.add(start)
            self.date.add(end)
            return True
        return False 