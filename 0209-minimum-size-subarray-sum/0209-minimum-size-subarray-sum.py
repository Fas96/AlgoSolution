class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        N,left,curSum=len(nums),0,0
        
        for i in range(N):
            curSum+=nums[i]
            while curSum >= target:
                ans=min(ans,i-left+1) 
                curSum-=nums[left]
                left+=1
        return ans if ans != float('inf') else 0