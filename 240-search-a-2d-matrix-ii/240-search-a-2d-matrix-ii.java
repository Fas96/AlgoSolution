class Solution {
   private int row;
  private int col;
  private boolean found=false;
  public boolean searchMatrix(int[][] matrix, int target) {
    col= matrix.length;
    row= matrix[0].length;
    int cnt=0;
    for (int i = 0; i < col; i++) {
      for (int j = 0; j < row; j++) {
        if(matrix[i][j]!=target){
          dfs(matrix,i,j,target);
        }else{
          found=true;
        }
      }
    }

    return  found;

  }
  private void dfs (int[][] grid, int i, int j,int target){
    if (i < 0 || j < 0 || i >= col || j >= row || grid[i][j] != target) return;
    grid[i][j] = 0;
    dfs(grid, i + 1, j,target);
    dfs(grid, i - 1, j,target);
    dfs(grid, i, j + 1,target);
    dfs(grid, i, j - 1,target);
  }

}