class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen = len(a)
        bLen = len(b)
        if aLen>=bLen:
            flag = 0
            b='0'*(aLen-bLen)+b
            c=['0']*aLen
            for i in range(aLen-1,-1,-1):
                c[i] = str(int(a[i])+int(b[i])+flag)
                
                if int(c[i])>1:
                    c[i]= str(int(c[i])-2)
                    flag =1
                if flag==1 and int(int(a[i])+int(b[i])+flag)<2:
                    flag=0
            if flag==1:
                c = ['1']+c
            return ''.join(c)
        if aLen<bLen:
            a='0'*(bLen-aLen)+a
            flag = 0
            c=['0']*bLen
            for i in range(bLen-1,-1,-1):
                print(i,a,b)
                c[i] = str(int(a[i])+int(b[i])+flag)
                if int(c[i])>1:
                    c[i]=str(int(c[i])-2)
                    flag =1
                if flag==1 and int(int(a[i])+int(b[i])+flag)<2:
                    flag=0
            if flag==1:
                c = ['1']+c
            return ''.join(c)