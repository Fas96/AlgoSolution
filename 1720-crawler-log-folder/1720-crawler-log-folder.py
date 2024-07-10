class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=0
        for p in logs:
            
            if p.startswith('..') and p.endswith('/'):
                if ans>0:
                    ans-=1
            elif p.endswith('/') and p!='./':
                ans+=1
        
        return ans

        