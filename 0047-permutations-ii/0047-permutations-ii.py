class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # permutations
        return list(set(permutations(nums, len(nums))))
