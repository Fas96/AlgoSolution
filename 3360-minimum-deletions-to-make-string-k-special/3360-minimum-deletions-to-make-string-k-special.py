class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq=Counter(word) 
        ans=len(word)
        for f in freq.values():
            sm=0
            for v in freq.values():
                if v<f:
                    sm+=v
                else:
                    sm+=max(0,v-f-k)
            ans=min(ans,sm)
        return ans
        