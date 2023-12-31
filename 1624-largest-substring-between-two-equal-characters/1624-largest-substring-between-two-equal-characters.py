class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max(s.rfind(c)-s.find(c)-1 for c in set(s))