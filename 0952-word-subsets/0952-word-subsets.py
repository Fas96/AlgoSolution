class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        fw2 =defaultdict(int)
        for x in words2:
            for k,v in Counter(x).items():
                if k not in fw2 or fw2[k]<v:
                    fw2[k]=v
        ans=[] 
        for w in words1:
            fw=Counter(w)
            cnt=True
            for k,v in fw2.items(): 
                if (k  not in fw) or  v>fw[k]:
                    cnt=False
                    break
                
            if cnt:
                ans.append(w)
        return ans
            
        