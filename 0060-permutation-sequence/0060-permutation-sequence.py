class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans=list(permutations(range(1,n+1)))
      
        return ''.join(map(str,ans[k-1]))