class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=0
        for p in logs:
            if p=='../':
                if ans>0: ans-=1
            elif p!='./': ans+=1
        
        return ans

        