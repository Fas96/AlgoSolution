class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current_pos = 0
        for c in s:
            current_pos = t.find(c, current_pos) + 1
            if current_pos == 0:
                return False
        return True