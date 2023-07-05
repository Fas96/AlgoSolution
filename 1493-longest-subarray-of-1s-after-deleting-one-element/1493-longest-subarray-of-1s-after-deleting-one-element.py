class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l,ans,n ,dd= 0,0,len(nums),defaultdict(int)
         
        for r in range(n):
            dd[nums[r]] += 1 
            while dd[0] > 1:
                dd[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
        