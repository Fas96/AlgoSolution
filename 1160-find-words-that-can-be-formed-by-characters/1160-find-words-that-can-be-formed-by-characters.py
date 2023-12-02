class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sm=0
        hm=Counter(chars)
        for w in words: 
            if not Counter(w) - hm:
                sm+=len(w)
                
        return sm
        