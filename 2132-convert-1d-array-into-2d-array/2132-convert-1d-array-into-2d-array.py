class Solution:
    def construct2DArray(self, og: List[int], m: int, n: int) -> List[List[int]]: 
        return [] if m*n != len(og) else [og[i:i+n] for i in range(0,m*n,n)]

            
        