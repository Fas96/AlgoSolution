class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        l, r = 0, 0
        res = 0
        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res