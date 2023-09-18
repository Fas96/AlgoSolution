class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        an=[]
        for i in range(len(mat)):
            an.append([i,mat[i].count(1)])
   
        an.sort(key=lambda x:x[1])

        return [k[0] for k in an][:k]
        