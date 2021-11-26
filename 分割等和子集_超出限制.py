class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        dp[i][j] 
        
        0 ->1 5 11 5
            0 6  
              0 
        '''
        m =  len(nums)
        sumNums = sum(nums)
        if sumNums%2==1:
            return False
        dp = [0]
        for i in nums:
            n = len(dp)
            for j in range(n):
                if dp[j]+i not in dp:
                    if i+dp[j] == sumNums//2:
                        return True
                    else:
                        dp.append(i+dp[j])
        return False