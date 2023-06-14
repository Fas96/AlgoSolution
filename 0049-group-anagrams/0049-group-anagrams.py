class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for ch in strs:
            sch = "".join(sorted(ch)) 
            if sch not in hm:
                hm[sch]=[ch]
            else:
                hm.get(sch).append(ch)
        return hm.values()
        