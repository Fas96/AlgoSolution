class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ll=[]
        N=len(mat)
        def bseach(row):
            L,H=0,len(row)-1
            while L<=H:
                M=(L+H)//2
                if row[M]==1:
                    L=M+1
                else:
                    H=M-1
            return L+1
            
        for idx in range(len(mat)):
            ll.append([idx,bseach(mat[idx])])
            
        ll.sort(key=lambda x: x[1])
   
        
        ans=[]
        for i in ll:
            ans.append(i[0])
            if len(ans)==k:
                break
        return ans
            