class Solution:
    def construct2DArray(self, og: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(og): return [] 
        return [og[i:i+n] for i in range(0,m*n,n)]

            
        