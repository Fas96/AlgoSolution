class Solution:
    def construct2DArray(self, og: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(og): return []
        ans=[] 
        ans=[]
        for i in range(0,m*n,n):
            ans.append(og[i:i+n])
        return ans

            
        