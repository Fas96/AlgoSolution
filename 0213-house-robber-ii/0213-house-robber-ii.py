class Solution:
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for b in nums:
            temp = max(rob1 + b, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        