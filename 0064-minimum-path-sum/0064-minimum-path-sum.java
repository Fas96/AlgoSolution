class Solution {
   public int minPathSum(int[][] grid) {
       return minPathSumHelper(grid,0,0);
    }

    private int minPathSumHelper(int[][] grid,int row, int col){
        if (row>=grid.length || col>=grid[0].length) return Integer.MAX_VALUE;
        else if (row==grid.length-1 && col==grid[0].length-1) return grid[row][col];
        else if (grid[row][col] < 101) grid[row][col] += 101 + Math.min(minPathSumHelper(grid, row+1, col), minPathSumHelper(grid, row, col+1));

        return grid[row][col] - 101;
    }
}