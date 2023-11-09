class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum(
            x * (x + 1) >> 1
            for _, grp in groupby(s)
            for x in [len(list(grp))]
        ) % (10**9 + 7)