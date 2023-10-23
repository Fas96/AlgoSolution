class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxProfit=0
        N=len(prices)
        while r<N:
            if prices[r]>prices[l]:
                maxProfit=max(maxProfit,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxProfit
                
                
                
            
            
        
        