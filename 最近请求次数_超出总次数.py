class RecentCounter:

    def __init__(self):
        self.time = [] #表示时间
        self.out = []


    def ping(self, t: int) -> int:
        self.time.append(t)
        tmp = 0
        for i in self.time:
            if i >=t-3000 and i<=t:
                tmp +=1
        self.out.append(tmp)
        return self.out[-1]




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)