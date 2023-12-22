class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        print(sorted(nums)[::2])
        return sum(sorted(nums)[::2])