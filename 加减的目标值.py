class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        正数-负数 =target
        正数+负数 = sum
        正数 =  (sum-target)/2
        '''
        numsLen = len(nums)
        numsSum = sum(nums)
        targetPos = int((numsSum +target)/2)
        if (numsSum +target)%2!=0:
            return 0
        dp = [[0 for i in range(targetPos+1)] for j in range(numsLen+1)]
        dp[0][0] = 1
        for i in range(1,numsLen+1):
            for j in range(targetPos+1):
                if j<nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-nums[i-1]]
        return dp[-1][-1]