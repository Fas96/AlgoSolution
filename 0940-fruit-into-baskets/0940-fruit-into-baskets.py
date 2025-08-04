class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N=len(fruits)
        frq=Counter()
        ans=float("-INF")
        lidx=0
        for i in range(N):
            frq[fruits[i]]+=1
            while  len(frq)>2:
                lf=fruits[lidx]
                frq[lf]-=1
                if frq[lf]==0:
                    del frq[lf] 
                lidx+=1 
            ans=max(ans,i-lidx+1)
        return ans
        