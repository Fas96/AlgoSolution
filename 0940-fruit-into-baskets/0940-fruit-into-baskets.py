from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        freq=Counter()
        ans=float("-INF")
        for i,fr in enumerate(fruits):
            freq[fr]+=1
            while len(freq)>2:
                lf=fruits[left]
                freq[lf]-=1
                if freq[lf]==0:
                    del freq[lf]
                left+=1
            ans=max(ans,i-left+1)
        return ans