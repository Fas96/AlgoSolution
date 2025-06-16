class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn=float('inf')
        mx=-1
        for x in nums:
            if x >mn:
                mx=max(mx,x-mn)
            mn=min(mn,x)
        return mx
        