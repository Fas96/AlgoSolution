class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        temp,maxProfit= -prices[0]-fee,0
        
        for idx in range(1,len(prices)):
            maxProfit=max(maxProfit,temp+prices[idx]) 
            temp=max(temp,maxProfit-prices[idx]-fee)
            
        return maxProfit
        