class Solution:
    def timechange(self,str:str)->int:
        hour = str.split(":")[0]
        minute = str.split(":")[1]
        AllMinutes = int(hour)*60 + int(minute)
        return AllMinutes

    def findMinDifference(self, timePoints: List[str]) -> int:
        maxDiffMinute = 24*60 
        timeTranInt = []
        for i in timePoints:
            tmp = self.timechange(i)
            timeTranInt.append(tmp)
        timeTranIntSort = sorted(timeTranInt)
        print(timeTranIntSort)
        minDiffminute = maxDiffMinute
        for i,item  in enumerate(timeTranIntSort):
            tmp1 = item - timeTranIntSort[i-1]
            if i==0:
                tmp1 = timeTranIntSort[i-1]-item
                tmp1 = min(tmp1,maxDiffMinute-tmp1)
            if tmp1 < minDiffminute :
                minDiffminute  = tmp1
        return minDiffminute