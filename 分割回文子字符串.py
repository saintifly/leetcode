class Solution(object):
    def isPalindrome(self,s):
        if s=='' or len(s)==1:
            return True
        if s[0]==s[-1]:
            return self.isPalindrome(s[1:-1])
        else:
            return False
    def PlaneSet(self,s):
        global sSetList
        sLen = len(s)
        sSetList = [[0 for i in range(sLen)] for j in range(sLen)]
        for i in range(sLen):
            for j in range(i,sLen):
                if i==j:
                    sSetList[i][j]=1
                if self.isPalindrome(s[i:j+1]) == True:
                    sSetList[i][j] = 1
        return sSetList
    def listAllSubset(self,s,startIndex):
        global resultRet,tmp,sSetList
        tmp1 = ''.join(tmp)
        if len(tmp1)>=len(s):
            resultRet.append(tmp)
            return
        for i,item in enumerate(sSetList[startIndex]):
            if item==1 and i>=startIndex:
                tmp.append(s[startIndex:i+1])
                startIndex = i + 1
            else:
                continue
            self.listAllSubset(s,startIndex)
            startIndex = startIndex - len(tmp[-1])
            tmp = tmp[:-1]
        return resultRet
                
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        global resultRet,tmp,sSetList
        sSetList = self.PlaneSet(s)
        tmp =[]
        resultRet =[]
        return self.listAllSubset(s,0)
