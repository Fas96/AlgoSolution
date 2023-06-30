class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ (n >> 1);
        if (((n + 1) & n) == 0):
            return True
        return False
        