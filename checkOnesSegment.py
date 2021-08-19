class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        lens = len(s)
        if lens <2:
            if int(s)==1:
                return True
            else:
                return False
        flag = 0
        count = 0
        for  i in s:
            if int(i)==1 and flag==0:
                count = count +1 
                flag=1
                continue
            if flag ==1 and int(i)==1:
                continue
            if flag == 1 and int(i)==0:
                flag=0
        if count == 1:
            return True
        else:
            return False