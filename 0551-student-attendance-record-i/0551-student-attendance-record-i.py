class Solution:
    def checkRecord(self, s: str) -> bool:
        f=Counter(s)
        print(f)
        return f['A']<2 and "LLL" not in s
        