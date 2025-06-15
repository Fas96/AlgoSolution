class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iter_t = iter(t)
        return all(c in iter_t for c in s)