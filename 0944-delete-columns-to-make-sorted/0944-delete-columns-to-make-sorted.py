class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        a=0
        for i in range(len(strs[0])): 
            ans=[]
            for j in range(len(strs)):
                ans.append(strs[j][i])
            if ans!=sorted(ans):
                a+=1
        return a
        