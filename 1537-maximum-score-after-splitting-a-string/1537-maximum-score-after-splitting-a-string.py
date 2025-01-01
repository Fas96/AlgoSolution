class Solution:
    def maxScore(self, s: str) -> int:
        return max([s[:i].count("0")+s[i:].count("1") for i in range(len(s)) if len(s[:i])>0 and len(s[i:])>0])
        