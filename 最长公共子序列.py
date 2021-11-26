class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        text1 -1  =dp[i]
        text2-1=dp[i]

        a=b dp[i]+1
        a!=b b[i] in a[b]

        '''
        s1 = len(text1)
        s2 = len(text2)
        print(s1,s2)
        dp =  [[0] * (s2 + 1) for _ in range(s1 + 1)]
        for i in range(s1):
            for j in range(s2):
                if text1[i]==text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                   dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) 
        return dp[-1][-1]