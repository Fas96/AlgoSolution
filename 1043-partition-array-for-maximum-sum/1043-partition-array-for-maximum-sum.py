class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            curmax=0
            for x in range(1,min(k,i)+1):
                curmax=max(curmax,arr[i-x])
                dp[i]=max(dp[i],dp[i-x]+curmax*x)
        return dp[n] 