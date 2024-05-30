class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        pf=[0]*(n+1)
        for i in range(n):
            pf[i+1]=pf[i]^arr[i]
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if pf[i]==pf[j+1]:
                    ans+=(j-i)
                    
        return ans
        