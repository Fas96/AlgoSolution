class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        ans=0
        for v in grid:
            ans+=len([n for n in v if n < 0])
        return ans
        