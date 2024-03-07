class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a1=list(word1)
        a2=list(word2)
        ans=[]
        for i in range(max(len(a1),len(a2))):
            if i<len(a1):
                ans.append(a1[i])
            if i<len(a2):
                ans.append(a2[i])
        return "".join(ans)
            