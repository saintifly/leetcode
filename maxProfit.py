class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_pric=len(prices)
        if len_pric<2:
            return 0
        Max = 0
        Min = prices[0]
        for i in range(len_pric):
            Max = max(Max, prices[i]-Min)
            Min = min(Min,prices[i])
        return Max