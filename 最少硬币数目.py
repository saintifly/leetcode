class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsLen = len(coins)
        coins = sorted(coins)
        dp = [10000 for i in range(amount+1)]
        if amount==0:
            return 0
        if amount<coins[0]:
            return -1
        dp[0] = 0
        for i in range(coinsLen):
            if coins[i]>amount:
                if dp[amount]==10000:
                    return -1
                else:
                    return dp[amount]
            dp[coins[i]]=1
            if i<coinsLen-1:
                for j in range(coins[i]+1,coins[i+1]):
                    for k in coins[:i+1]:
                        if j>amount:
                            if dp[amount]==10000:
                                return -1
                            return dp[amount]
                        if dp[j-k]==10000:
                            continue
                        dp[j] = min(dp[j-k],dp[j])+1
        for i in range(coins[-1]+1,amount+1):
            for j in coins:
                if dp[i-j]==10000:
                    continue
                else:
                    dp[i] = min(dp[i],dp[i-j])
            if dp[i]!=10000:
                    dp[i] = dp[i]+1
        if dp[-1]==10000:
            return -1
        else:
            return dp[-1]