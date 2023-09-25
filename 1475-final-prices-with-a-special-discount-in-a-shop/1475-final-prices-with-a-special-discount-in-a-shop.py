class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer=[-1]* len(prices)
        check = True
        stk=[]
        for i in range(len(prices)):
            while stk and prices[stk[-1]]>=prices[i]:
                answer[stk[-1]]=(prices[stk[-1]]-prices[i])
                stk.pop()
            stk.append(i)
        for i in range(len(prices)):
            if answer[i]==-1:
                answer[i]=prices[i]
        return answer