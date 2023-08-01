class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans=permutations(range(1,n+1))
        for i in range(k-1):
            next(ans)
        return ''.join(map(str,next(ans)))