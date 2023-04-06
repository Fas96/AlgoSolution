class Solution {
    public int closedIsland(int[][] grid) {
       int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 0) {
                    if (dfs(grid, i, j)) count++;
                }
            }
        }
        return count;

    }

    private boolean dfs(int[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) return false;
        if (grid[i][j] == 1) return true;
        grid[i][j] = 1;
        boolean res = true;
        res &= dfs(grid, i + 1, j);
        res &= dfs(grid, i - 1, j);
        res &= dfs(grid, i, j + 1);
        res &= dfs(grid, i, j - 1);
        return res;
    }
}