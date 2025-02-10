from functools import reduce

class Solution:
    def clearDigits(self, s: str) -> str:
        return reduce(lambda res, c: res[:-1] if c.isnumeric() and res else res + c, s, "")
