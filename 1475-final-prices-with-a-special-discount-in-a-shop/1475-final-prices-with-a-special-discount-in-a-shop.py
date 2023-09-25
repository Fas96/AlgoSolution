class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=prices
        check = True
        stk=[]
        for i in range(len(prices)):
            while stk and prices[stk[-1]]>=prices[i]:
                answer[stk[-1]]=(prices[stk[-1]]-prices[i])
                stk.pop()
            stk.append(i)
 
        return answer