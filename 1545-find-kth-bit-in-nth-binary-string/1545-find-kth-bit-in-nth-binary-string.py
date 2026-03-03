class Solution:
    def findKthBit(self, N: int, K: int) -> str:
        ans = 1
        mid = (1 << (N - 1))
        while K > 1:
            if K == mid: return str(ans)
            if K > mid: 
                K = 2 * mid - K
                ans ^= 1
            mid >>= 1
        return str(ans^1)