class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        numsLen = len(nums)
        numsSum = sum(nums)
        targetPos = int((numsSum +target)/2)
        if (numsSum +target)%2!=0 or targetPos<0:
            return 0
        dp = [0 for j in range(targetPos+1)]
        dp[0] = 1
        for i in nums:
            for j in range(targetPos,i-1,-1):
                dp[j] = dp[j] + dp[j-i]
        print(dp)
        return dp[-1]