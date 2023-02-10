class Solution {
  public int maxDistance(int[][] grid) {
        Queue<Point> q=new ArrayDeque<>();
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1){
                    q.add(new Point(i,j));
                }
            }
        }
        if(q.size()==grid.length*grid.length){
            return -1;
        }
        int ans=-1;
         int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while(!q.isEmpty()){
            int size=q.size();
            for(int i=0;i<size;i++){
                Point point=q.remove();
                for(int[] d:dir){
                    int x1=d[0]+point.x;
                    int y1=d[1]+point.y;
                    if(x1>=0&&y1>=0&&x1<grid.length&&y1<grid[0].length&&grid[x1][y1]==0){
                        grid[x1][y1]=1;
                        q.add(new Point(x1,y1));
                    }
                }
            }
            ans++;
        }
        return ans;
    }
    class Point{
        int x;
        int y;
        public Point(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
}