from itertools import product
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = {s[i:i+k] for i in range(len(s) - k + 1)}
        return len(seen) == 2 ** k