class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        
    int x=click[0],y=click[1];
        if(board[x][y]=='M'){
            board[x][y]='X';
        }else{
            dfs(board,x,y);
        }
        return board;
    }

    private void dfs(char[][] board, int x, int y) {
        int count=0;
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if(i==0&&j==0)continue;
                if(x+i<0||x+i>=board.length||y+j<0||y+j>=board[0].length)continue;
                if(board[x+i][y+j]=='M'||board[x+i][y+j]=='X')count++;
            }
        }
        if(count>0){
            board[x][y]=(char)(count+'0');
        }else{
            board[x][y]='B';
            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1; j++) {
                    if(i==0&&j==0)continue;
                    if(x+i<0||x+i>=board.length||y+j<0||y+j>=board[0].length)continue;
                    if(board[x+i][y+j]=='E'){
                        dfs(board,x+i,y+j);
                    }
                }
            }
        }
    }
//         int[][] dirs={{0,1},{0,-1},{1,0},{-1,0}};
    
//     M=X
//     E= {all dir}  and change B and all dir M
        
//     E all dirs has M >=1 :('1' to '8') number of adj
    
//     return of no more sqrs will be revealed
}