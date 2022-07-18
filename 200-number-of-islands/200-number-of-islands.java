class Solution {
    private int row;
  private int col;
    public int numIslands(char[][] grid) {

       col= grid.length;
       row= grid[0].length;
      int max=0;
      int cnt=0;
      for (int i = 0; i < col; i++) {
        for (int j = 0; j < row; j++) {
          if(grid[i][j]=='1'){
            dfs(grid,i,j);
            cnt+=1;
          }


        }
      }

      return cnt;
    }
    private void dfs (char[][] grid, int i, int j){
      if (i < 0 || j < 0 || i >= col || j >= row || grid[i][j] != '1') return;
      grid[i][j] = '0';
      dfs(grid, i + 1, j);
      dfs(grid, i - 1, j);
      dfs(grid, i, j + 1);
      dfs(grid, i, j - 1);
    }
}