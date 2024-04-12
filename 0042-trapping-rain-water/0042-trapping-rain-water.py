class Solution:
    def trap(self, height: List[int]) -> int:
        N=len(height)
        stk=[]
        ans=0
        for i,n in enumerate(height): 
            while stk and stk[-1][1]<n:
                idx,num=stk.pop()
                if stk:
                    low=min(n,stk[-1][1])
                    filled=low-num
                    width=i-stk[-1][0]-1
                    ans+=(filled*width)
            stk+=[(i,n)]
            
        return ans
        