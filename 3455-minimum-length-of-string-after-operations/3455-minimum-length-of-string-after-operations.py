class Solution:
    def minimumLength(self, s: str) -> int: 
        if len(s)<3: return len(s)
        return sum(1 if x % 2 else 2 for x in Counter(s).values())

