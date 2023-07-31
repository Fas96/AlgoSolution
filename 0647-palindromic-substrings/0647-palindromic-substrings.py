class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(2):
                l, r = i, i + j
                while l >= 0 and r < n and s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
        return ans
        