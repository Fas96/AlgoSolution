class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=[x*x for x  in nums]
        return sorted(n)
        