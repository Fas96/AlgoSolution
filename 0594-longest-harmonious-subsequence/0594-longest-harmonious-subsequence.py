class Solution:
    def findLHS(self, nums: List[int]) -> int:
        f=Counter(nums)
        ans=0
        for x in f:
            if x+1 in f:
                ans=max(ans,f[x]+f[x+1])
        return ans