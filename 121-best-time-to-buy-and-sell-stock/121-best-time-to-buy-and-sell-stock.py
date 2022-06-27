class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        r = 0
        
        buy=prices[0]
        for i in range(len(prices)):
            buy=min(prices[i],buy)
            r = max(r, prices[i] - buy)
        return r