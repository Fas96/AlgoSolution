class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque((i, j) for j in range(n) for i in range(m) if mat[i][j] == 0)
        mp = [[0 if mat[i][j] == 0 else float("-inf") for j in range(n)] for i in range(m)]
        while q:
            i, j = q.popleft()
            for ci, cj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ci < m and 0 <= cj < n and mp[ci][cj] == float("-inf"):
                    mp[ci][cj] = mp[i][j] + 1
                    q.append((ci, cj))
        return mp