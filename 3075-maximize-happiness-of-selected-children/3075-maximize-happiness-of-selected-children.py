class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()
        N,idx=len(happiness),0
        times,keep,ans=0,0,float('-inf') 
        while k:
            cur=happiness[N-1-times] 
            keep+=(cur-times)
            ans=max(ans,keep)
            times+=1 
            k-=1
        return ans
            
            