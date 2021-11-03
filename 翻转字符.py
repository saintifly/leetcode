class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for i in range(2)] for i in range(n)]
        if s[0]=='0':
            dp[0][1] = 1
        if s[0]=='1':
            dp[0][0] = 1
        for i in range(n):
            if s[i]=='0':
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][0],dp[i-1][1])+1
            if s[i]=='1':
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = min(dp[i-1][0],dp[i-1][1])
        return min(dp[i])

