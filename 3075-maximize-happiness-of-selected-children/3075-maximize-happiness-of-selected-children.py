class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()
        times,keep,ans=0,0,float('-inf')
        print(happiness)
        while k>0:
            cur=happiness.pop()
            print(times)
            keep+=(cur-times)
            ans=max(ans,keep)
            times+=1
            k-=1
        return ans
            
            