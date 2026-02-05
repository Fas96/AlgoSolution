class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + v) % len(nums)] for i, v in enumerate(nums)]