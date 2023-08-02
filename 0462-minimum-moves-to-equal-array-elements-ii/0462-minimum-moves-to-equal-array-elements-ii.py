class Solution:
    def minMoves2(self, nums: List[int]) -> int: 
        mid=len(nums)//2
        nums.sort()
        return sum(abs(nums[mid] - i) for i in nums)
        