class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        s3[n+m] = s3[n-1][m]+s1[-1] or  s3[n+m] = s3[n][m-1]+s2[-1]
        '''
        s3Len = len(s3)
        s2Len = len(s2)
        s1Len = len(s1)
        if s3Len != s2Len+s1Len:
            return False
        dp = [[False for i in range(s2Len+1)] for j in range(s1Len+1)]
        dp[0][0]=True
        for i in range(s1Len):
            if s1[i]==s3[i]:
                dp[i+1][0]=True
            else:
                break
        for i in range(s2Len):
            if s2[i]==s3[i]:
                dp[0][i+1]=True
            else:
                break
        print(dp)
        for i in range(0,s1Len):
            for j in range(0,s2Len):
                if (s3[i+j+1]==s1[i] and dp[i][j+1]==True) or (s3[i+j+1]==s2[j] and  dp[i+1][j]==True): 
                    dp[i+1][j+1]=True
                else:
                     dp[i+1][j+1]=False
        return dp[s1Len][s2Len]