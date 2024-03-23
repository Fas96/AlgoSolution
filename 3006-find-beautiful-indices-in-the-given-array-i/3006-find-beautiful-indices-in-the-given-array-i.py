class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans=[]
        aa,ab=[],[]
        for i in range(len(s)):
            if s[i] == a[0] and s[i:i + len(a)] == a:
                aa.append(i)
            if s[i] == b[0] and s[i:i + len(b)] == b:
                ab.append(i)
        print(aa,ab)
        for i in aa:
            for j in ab:
                if abs(i-j)<=k:
                    ans.append(i)
                    break
        return ans