class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return int(sum((count * (count - 1) / 2) * 8 for count in Counter(a * b for a, b in combinations(nums, 2)).values()))