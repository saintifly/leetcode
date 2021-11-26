class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        dp[i][j] 
        
        0 ->1 5 11 5
            0 6  
              0 
        '''
        sumNums = sum(nums)
        if sumNums%2==1:
            return False
        dp = {0}
        tmp = set()
        half = sumNums//2
        for i in nums:
            for j in dp:
                if j+i not in dp:
                    if i+j == half :
                        return True
                    else:
                        tmp.add(i+j)
            dp = dp.union(tmp)
        return False