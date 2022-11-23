class Solution {
    public boolean isValidSudoku(char[][] board) {
       return solveSudoku(board,board[0].length); 
    }
    
    public boolean solveSudoku(char[][] board,int N) {

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) { 
       if (board[i][j] != '.' && !isValidPlacement(board, board[i][j], i, j)) return false;

        }
      }
    
    return true;
  }

  private boolean isNumInRow(char[][] board,char number,int row, int column){
    for (int i = 0; i < board.length; i++) {
      if(column != i && board[row][i]==number)return true;
    }
    return false;
  }
  private boolean isNumInColumn(char[][] board,char number, int row, int col){
    for (int i = 0; i < board.length; i++) {
      if(row != i && board[i][col]==number)return true;
    }
    return false;
  }
  private boolean isNumInBox(char[][] board,char number,int row,int col){
    int localRow=row-row%3;
    int localCol=col-col%3;

    for (int i = localRow; i < localRow+3; i++) {
      for (int j = localCol; j < localCol+3; j++) {
        if(row != i && col != j && board[i][j]==number)return true;
      }
    }
    return false;
  }
  private boolean isValidPlacement(char[][] board,char number,int row,int col){
    return !isNumInRow(board, number,row,col) &&
        !isNumInColumn( board, number,row, col)&&
      !isNumInBox(board,number,row,col);
  }
}