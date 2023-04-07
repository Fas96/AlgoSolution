class Solution {
    public int numEnclaves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for (int i = 0; i < m; i++) {
            dfs(grid, i, 0);
            dfs(grid, i, n - 1);
        }
        for (int i = 0; i < n; i++) {
            dfs(grid, 0, i);
            dfs(grid, m - 1, i);
        }
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) count++;
            }
        }
        return count;

    }

    private void dfs(int[][] grid, int i, int i1) {
        if (i < 0 || i >= grid.length || i1 < 0 || i1 >= grid[0].length || grid[i][i1] == 0) return;
        grid[i][i1] = 0;
        dfs(grid, i + 1, i1);
        dfs(grid, i - 1, i1);
        dfs(grid, i, i1 + 1);
        dfs(grid, i, i1 - 1);
    }
}