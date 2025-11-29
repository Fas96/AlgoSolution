class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if(sum(nums)<k):return sum(nums)
        return min(sum(nums)%k,sum(nums)-(sum(nums)%k))
        