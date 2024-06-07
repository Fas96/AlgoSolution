class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        roots = set(d)  
        words = s.split() 
        for i in range(len(words)):
            for root in roots:
                if words[i].startswith(root): 
                    words[i] = root 
        return ' '.join(words)       
        