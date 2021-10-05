class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = size
        self.a =  []


    def next(self, val: int) -> float:
        if (len(self.a)<self.window):
            self.a.append(val)
            out = sum(self.a)/len(self.a)
        else:
            self.a.remove(self.a[0])
            self.a.append(val)
            out = sum(self.a)/self.window
        return out