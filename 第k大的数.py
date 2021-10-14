class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        from sortedcontainers import SortedList
        self.date = SortedList()
        for i in nums:
            self.date.add(i)
        self.k = k


    def add(self, val: int) -> int:
        self.date.add(val)
        return self.date[-self.k]
