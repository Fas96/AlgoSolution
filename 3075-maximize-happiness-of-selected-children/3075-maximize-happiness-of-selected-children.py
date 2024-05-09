class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()
        times,keep,ans=0,0,float('-inf') 
        while k>0:
            cur=happiness.pop() 
            keep+=(cur-times)
            ans=max(ans,keep)
            times+=1
            k-=1
        return ans
            
            