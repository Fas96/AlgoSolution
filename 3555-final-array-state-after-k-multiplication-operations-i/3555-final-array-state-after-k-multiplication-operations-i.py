class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            midx=nums.index(min(nums))
            nums[midx]*=multiplier
        return nums 
            