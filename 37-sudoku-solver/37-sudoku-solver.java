class Solution {
    public void solveSudoku(char[][] board) {
       solveSudoku(board,board.length);
        
  }
  public boolean solveSudoku(char[][] board,int N) {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (board[i][j] == '.'){
          for (int tryNum = 1; tryNum <= N; tryNum++) {
            if(isValidPlacement(board,String.valueOf( tryNum).charAt(0),i,j)){
              board[i][j]=  String.valueOf( tryNum).charAt(0);
              if(solveSudoku(board,N)){
                return true;
              }else{
                board[i][j]='.';
              }
            }
          }
          return false;

        }
      }
    }
    return true;
  }

  private boolean isNumInRow(char[][] board,char number,int row){
    for (int i = 0; i < board.length; i++) {
      if(board[row][i]==number)return true;
    }
    return false;
  }
  private boolean isNumInColumn(char[][] board,char number,int col){
    for (int i = 0; i < board.length; i++) {
      if(board[i][col]==number)return true;
    }
    return false;
  }
  private boolean isNumInBox(char[][] board,char number,int row,int col){
    int localRow=row-row%3;
    int localCol=col-col%3;
    for (int i = localRow; i < localRow+3; i++) {
      for (int j = localCol; j < localCol+3; j++) {
        if(board[i][j]==number)return true;
      }
    }
    return false;
  }
  private boolean isValidPlacement(char[][] board,char number,int row,int col){
    return !isNumInRow(board, number,row) &&
        !isNumInColumn( board, number, col)&&
      !isNumInBox(board,number,row,col);
  }
}