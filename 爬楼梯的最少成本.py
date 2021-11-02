class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        costLen = len(cost)
        current = 0
        past = 0
        for i in range(2,costLen+1):
            tmp = min(current+cost[i-1],past+cost[i-2])
            past = current
            current = tmp
        return current