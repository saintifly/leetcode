class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle[-1])
        dp = [[0 for j in range(i+1)] for i in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(m):
            for j in range(i+1):
                if i>0 :
                    if j>0 and j-1<i-1:
                        dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
                        continue
                    if j==0:
                        dp[i][j]=dp[i-1][j] + triangle[i][j]
                    else:
                        dp[i][j]=dp[i-1][j-1] + triangle[i][j]
        return min(dp[-1])