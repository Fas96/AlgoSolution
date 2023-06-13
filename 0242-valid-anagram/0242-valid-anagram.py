class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs,ht ={},{}
        for ch in s:
            if ch in hs:
                hs[ch]+=1
            else:
                hs[ch] = 1
                
        for ch in t:
            if ch in ht:
                ht[ch] += 1
            else:
                ht[ch] = 1
        return ht == hs
                
        
        