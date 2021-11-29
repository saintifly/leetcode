class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        coinsLen = len(nums)
        coins = sorted(nums)
        dp = [0 for i in range(target+1)]
        if target==0:
            return 0
        if target<coins[0]:
            return 0
        dp[0] = 0
        print(coins)
        for i in range(coinsLen):
            if coins[i]<=target:
                dp[coins[i]]=dp[coins[i]]+1
            for j in range(coins[i-1]+1,coins[i]+1):
                for k in coins[:i]:
                    dp[j] = dp[j]+dp[j-k]
                if j+1>target:
                    return dp[target]
        for i in range(coins[-1]+1,target+1):
            for j in coins:
                dp[i] = dp[i]+dp[i-j]
        return dp[-1]