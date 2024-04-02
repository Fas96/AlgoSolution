class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fo=0
        r,c=len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fo+=1
        q.append((-1,-1))
        me=-1
        dirr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            cr,cc=q.popleft()
            if cr==-1:
                me+=1
                if q: q.append((-1,-1))
            else:
                for ii,jj in dirr:
                    ni,nj=cr+ii,cc+jj
                    if r>ni>=0 and c>nj>=0 and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        fo-=1
                        q.append((ni,nj))
        return me if fo==0 else -1
        