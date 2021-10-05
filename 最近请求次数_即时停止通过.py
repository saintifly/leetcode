class RecentCounter:

    def __init__(self):
        self.time = [] #表示时间
        self.out = []


    def ping(self, t: int) -> int:
        self.time.append(t)
        tmp = 0
        for i in reversed(self.time):
            if i <t-3000:
                break
            tmp +=1
        self.out.append(tmp)
        return self.out[-1]
