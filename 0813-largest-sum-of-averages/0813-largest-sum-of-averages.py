class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        m=len(nums)
        c={}
        def go(idx,k):
            if (idx,k) in c:
                return c[(idx,k)]
            if idx==m:
                return 0.0 if k==0 else float("-inf") 
            if k==0: return float('-inf')
            ans=0
            t=0
            for i in range(idx,m):
                t+=nums[i]
                av=t/(i-idx+1)
                ans=max(ans, av + go(i + 1, k - 1))
            c[(idx,k)]=ans
            return ans
        
        return go(0,k)
        