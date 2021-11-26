class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        动态规则

        dp[i][j] 代表t[j:] 在 s[i:]中有n种
        '''
        m = len(s)
        n = len(t) 
        if n > m :
            return 0
        dp = [[0 for i in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if j==n:
                    dp[i][j]=1
                    continue
                if i==m:
                    dp[i][j]=0
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if i<m and j<n:
                    
                    if s[i]==t[j]:
                        dp[i][j] = dp[i+1][j+1] +dp[i+1][j]
                    else:
                        dp[i][j] =  dp[i+1][j]
        return dp[0][0]