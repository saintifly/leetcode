class Solution:

    def minCut(self, s: str) -> int:
        n = len(s)
        f = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            f[i][i] = True

        for r in range(n):
            for l in range(r - 1, -1, -1):
                if s[l] == s[r]:
                    if l + 1 == r:
                        f[l][r] = True
                    else:
                        f[l][r] = f[l + 1][r - 1]
        dp = [n for i in range(n)]
        for r in range(n):
            if f[0][r] == True:
                dp[r] = 0
            else:
                for l in range(r):
                    if f[l + 1][r] == True:
                        dp[r] = min(dp[r], dp[l] + 1)
        return dp[n-1]
