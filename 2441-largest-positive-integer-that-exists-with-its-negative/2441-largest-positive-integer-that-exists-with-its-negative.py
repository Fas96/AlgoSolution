class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans=float('-inf')
        freq=Counter(nums)
        for k,v in freq.items():
            if k in freq and -k in freq:
                ans=max(ans,k)
        return ans if ans!=float(-inf) else -1
        
        