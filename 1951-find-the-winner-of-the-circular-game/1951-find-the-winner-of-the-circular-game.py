class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def go(n, k):
            if n == 1: return 0
            return (go(n - 1, k) + k) % n

        return go(n, k) + 1