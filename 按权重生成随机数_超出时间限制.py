class Solution:

    def __init__(self, w: List[int]):
        self.wSort = sorted(w)
        self.wSum = sum(w)
        self.wCout = w
        for i,item in enumerate(self.wSort):
            if i>0:
                self.wSort[i] = self.wSort[i-1]+self.wSort[i]
                self.wCout[i] = (self.wSort[i-1],self.wSort[i])
            else:
                self.wCout[0] = (0,self.wSort[0])


        # self.wCout = list((self.wSort,w))
        print(self.wCout)

    def pickIndex(self) -> int:
        import random
        i = random.randint(0,self.wSum)
        start = 0
        end = len(self.wCout)-1
        while(start < end-1):
            mid = start + (end-start)//2
            if self.wCout[mid][0]<i<self.wCout[mid][1]:
                return mid
            if i <self.wCout[mid][0]:
                end = mid
            if i >self.wCout[mid][1]:
                start = mid
        if self.wCout[start][0]<=i<=self.wCout[start][1]:
            return start
        else:
            return end
        return 



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()