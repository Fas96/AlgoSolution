class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 for j in range(len(nums)) if nums[j] < nums[i]) for i in range(len(nums))]
        