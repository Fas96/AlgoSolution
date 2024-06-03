class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sn,tn,sIdx,tIdx=len(s),len(t),0,0
         
        while sIdx<sn and tIdx<tn:
            if s[sIdx]==t[tIdx]:
                tIdx+=1
            sIdx+=1
        
        return tn-tIdx