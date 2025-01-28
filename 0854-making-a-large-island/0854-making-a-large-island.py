class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid:
            return 0
         
        component_size = {}
        component_id = 2
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
 
        def dfs(x: int, y: int, comp_id: int) -> int:
            if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = comp_id
            size = 1
            for dx, dy in directions:
                size += dfs(x + dx, y + dy, comp_id)
            return size
 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    component_size[component_id] = dfs(i, j, component_id)
                    component_id += 1 
        max_area = max(component_size.values(), default=0)
 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_components = set()
                    area = 1  
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            comp_id = grid[ni][nj]
                            if comp_id not in seen_components:
                                seen_components.add(comp_id)
                                area += component_size[comp_id]
                    max_area = max(max_area, area)

        return max_area