class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return max(sum(ceil(f/3) if f>1 else -inf for f in Counter(nums).values()),-1)