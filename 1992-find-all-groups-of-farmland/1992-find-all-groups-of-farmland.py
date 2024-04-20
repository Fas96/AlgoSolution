class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or land[row][col] != 1:
                return 
            land[row][col] = 2 
            nonlocal top_left, bottom_right
            top_left = [min(top_left[0], row), min(top_left[1], col)]
            bottom_right = [max(bottom_right[0], row), max(bottom_right[1], col)] 
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        m, n = len(land), len(land[0])
        result = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    top_left = [i, j]
                    bottom_right = [i, j]
                    dfs(i, j)
                    result.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])
        
        return result