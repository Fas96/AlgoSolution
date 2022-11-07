class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
      int n=grid.length;
        if(grid[0][0]==1||grid[n-1][n-1]==1) return -1;
        if(n==1) return 1;
        int[][] dirs={{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
        int[][] visited=new int[n][n];
        visited[0][0]=1;
        int res=1;
        while(true){
            res++;
            boolean flag=false;
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    if(visited[i][j]==res-1){
                        for(int[] dir:dirs){
                            int x=i+dir[0];
                            int y=j+dir[1];
                            if(x>=0&&x<n&&y>=0&&y<n&&grid[x][y]==0&&visited[x][y]==0){
                                if(x==n-1&&y==n-1) return res;
                                visited[x][y]=res;
                                flag=true;
                            }
                        }
                    }
                }
            }
            if(!flag) return -1;
        }
          
    }
}