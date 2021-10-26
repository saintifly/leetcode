class Solution:

    def __init__(self, w: List[int]):
        self.wSum = sum(w)
        self.wCout = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        import random,bisect
        i = random.randint(1,self.wSum)
        return bisect.bisect_left(self.wCout,i)