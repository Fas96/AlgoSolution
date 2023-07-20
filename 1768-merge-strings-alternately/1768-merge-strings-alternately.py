class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=len(word1)
        w2=len(word2) 
        s=""
        cnt=0
        
        for i in range(min(w1,w2)):
            s+=(word1[i])
            s+=(word2[i])
            cnt+=1
            
        for i in range(cnt,w1):
            s+=(word1[i])
        for i in range(cnt,w2):
            s+=(word2[i])
        return s
            
         
        
            
        
        