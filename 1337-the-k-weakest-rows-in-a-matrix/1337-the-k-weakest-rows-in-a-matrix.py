class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ll=[]
 
            
        for idx in range(len(mat)):
            ll.append([idx, mat[idx].count(1)])
            
        ll.sort(key=lambda x: x[1])
 
        return [v[0] for v in ll[:k]]
            