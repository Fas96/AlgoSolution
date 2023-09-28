class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans,N,target=0,len(grid[0]),0 
        for n in grid: 
            L,R= 0,len(n)-1 
            while L<=R:
                M=(L+R)//2 
                if n[M]<target:
                    R=M-1
                else:
                    L=M+1
            ans+=(N-L)
        return ans
        
  