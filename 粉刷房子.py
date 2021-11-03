class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n==1:
            return min(costs[0])
        if n==0:
            return 0
        dp = [[0 for i in range(3)] for i in range(n)]
        dp[0] = costs[0]
        for i in range(1,n):
            dp[i][0] = min(dp[i-1][1],dp[i-1][2])+costs[i][0]
            dp[i][1] = min(dp[i-1][0],dp[i-1][2])+costs[i][1]
            dp[i][2] = min(dp[i-1][1],dp[i-1][0])+costs[i][2]
        return min(dp[i])