class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans=[]
        aa,ba=[i for i in range(len(s)) if s.startswith(a,i)],[i for i in range(len(s)) if s.startswith(b,i)] 
  
        for i in aa:
            for j in ba:
                if abs(j-i)<=k:
                    ans.append(i)
                    break
        return sorted(list(set(ans)))
                
                
        