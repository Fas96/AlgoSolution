class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans=float('-inf')
        for c in nums:
            if c in nums and -c in nums:
                ans=max(c,ans)
        return ans if ans!=float(-inf) else -1
        
        