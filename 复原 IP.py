class Solution:
    def PathSet(self,s)->List[int]:
        sLen = len(s)
        sSetList = [[0 for i in range(sLen)] for j in range(sLen)]
        for i in range(sLen):
            for j in range(i,sLen):
                if  len(s[i:j+1])<4 and int(s[i:j+1])>=0 and int(s[i:j+1])<=255:
                    if len(s[i:j+1])>1 and int(s[i])==0:
                        continue
                    else:
                        sSetList[i][j]=1
        return sSetList
    
    def listAllSubIp(self,s:str,startIndex:int)->List[str]:
        global resultRet,tmp,sSetList
        print(resultRet)
        if len(tmp)>=4 or len(''.join(tmp))>=len(s):
            if len(''.join(tmp)) ==len(s) and len(tmp) ==4:
                resultRet.append('.'.join(tmp))
            return resultRet
        for i,item in enumerate(sSetList[startIndex]):
            if item==1 and i>=startIndex:
                tmp.append(s[startIndex:i+1])
                startIndex = i+1
            else:
                continue
            self.listAllSubIp(s,startIndex)
            startIndex =startIndex-len(tmp[-1])
            tmp=tmp[:-1]
        return resultRet

    def restoreIpAddresses(self, s: str) -> List[str]:
        global resultRet,tmp,sSetList
        sSetList = self.PathSet(s)
        tmp =[]
        resultRet = []
        return self.listAllSubIp(s,0)

        