class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for i in range(m) ]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j>0:
                    dp[0][j] = grid[0][j]+dp[0][j-1]
                if j==0 and i>0:
                    dp[i][0] = grid[i][0]+dp[i-1][0]
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]