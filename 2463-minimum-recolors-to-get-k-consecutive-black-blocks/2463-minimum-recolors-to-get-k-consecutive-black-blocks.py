class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=float("inf")
        n=len(blocks)
        for i in range(n-k+1):
            b=blocks[i:i+k]
            ans=min(ans,b.count('W'))
        return ans

        
        