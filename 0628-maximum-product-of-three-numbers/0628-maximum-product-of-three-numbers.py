class Solution:
    def maximumProduct(self, nums: List[int]) -> int: 
        nums.sort()
        hi3 = nums[-1] * nums[-2] * nums[-3]
        low2h1 = nums[0] * nums[1] * nums[-1]
        return max(low2h1, hi3)
        