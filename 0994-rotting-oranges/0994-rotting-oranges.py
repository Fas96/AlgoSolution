class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        r,c=len(grid),len(grid[0])
        fo=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fo+=1
        mo=-1
        q.append((-1,-1))
        while q:
            cr,cc=q.popleft()
            if cr==-1:
                mo+=1
                if q:q.append((-1,-1))
            else:
                assert (cr>-1 and cc>-1),"false"
                for d1,d2 in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ni,nj=cr+d1,cc+d2
                    if r>ni>=0 and c>nj>=0 and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        fo-=1
                        q.append((ni,nj))
        return mo if fo==0 else -1
        