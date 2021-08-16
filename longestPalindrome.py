class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenInputS = len(s)
        if lenInputS <2:
            return s
        palindList = [[0]*lenInputS for i in range(lenInputS)]
        maxPalindStart = 0
        maxPalindLen = 1
        
        for j in range(lenInputS):
            for i in range(j):
                if s[i]==s[j] and (j-i+1<3 or palindList[i+1][j-1]==1):
                    palindList[i][j] = 1
                    if maxPalindLen < j-i+1:
                        maxPalindLen = j -i +1
                        maxPalindStart = i
            palindList[j][j]=1
        return s[maxPalindStart:maxPalindStart+maxPalindLen]