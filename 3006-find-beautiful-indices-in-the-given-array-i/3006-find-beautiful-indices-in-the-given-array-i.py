class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans=[]
        aa,ba=[],[]
        for i in range(len(s)):
            if (s[i]==a[0] and s[i:i+len(a)]==a):
                aa.append(i)
            if (s[i]==b[0] and s[i:i+len(b)]==b):
                ba.append(i)
  
        for i in aa:
            for j in ba:
                if abs(j-i)<=k:
                    ans.append(i)
                    break
        return sorted(list(set(ans)))
                
                
        