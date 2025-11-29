class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sm=sum(nums)
        if(sm<k):return sm
        return min(sm%k,sm-(sm%k))
        