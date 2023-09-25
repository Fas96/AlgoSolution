class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=[-1]* len(prices)
        check = True
        for i in range(len(prices)):
            check=True
            for j in range(i+1,len(prices)):
                if answer[i]!=-1:
                    break
                if prices[i] >= prices[j]:
                    answer[i] = (prices[i] - prices[j]) 
                    check=False
            if check:
                answer[i]=prices[i]
            
        
        return answer