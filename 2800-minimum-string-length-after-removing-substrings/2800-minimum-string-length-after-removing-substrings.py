class Solution:
    def minLength(self, s: str) -> int:

        while ("AB" in s or "CD" in s) and len(s)>0:
            if "AB" in s:
                s=s.replace("AB","")
            if "CD" in s:
                s=s.replace("CD","")
        return len(s)
        