class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        que = deque()
        mat = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isWater[i][j] ==1:
                    que.append((i, j, 0))
                    mat[i][j] = 0

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
        while que:
            r, c, height = que.popleft()
            
            for dr, dc in dir:
                xr, xc = r + dr, c + dc
                if 0 <=xr < n and 0 <= xc < m and mat[xr][xc] == -1:
                    mat[xr][xc] = height + 1
                    que.append((xr, xc, height + 1))
        return mat
        