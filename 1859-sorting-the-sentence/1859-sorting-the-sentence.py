class Solution:
    def sortSentence(self, s: str) -> str:
        arr=sorted(s.split(" "),key=lambda x: x[len(x)-1])
        
        res=""
        for x in arr:
            res+=(x[:len(x)-1]+' ')
        
        return res.strip()
        
        