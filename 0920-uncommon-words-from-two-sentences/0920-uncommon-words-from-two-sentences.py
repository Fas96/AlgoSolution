class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        f,s=Counter(s1.split(' ')),Counter(s2.split(' '))
        print(f)
        ans=[]
        for k,v in f.items():
            if v>1: continue
            if k in s and k in f: continue
            ans.append(k)
        for k,v in s.items():
            if v>1: continue
            if k in s and k in f: continue
            ans.append(k)


        return ans