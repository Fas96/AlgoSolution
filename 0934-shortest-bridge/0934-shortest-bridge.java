class Solution {
    public int shortestBridge(int[][] grid) {
          int n = grid.length;
        int m = grid[0].length;
        boolean[][] visited = new boolean[n][m];
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        Queue<int[]> q = new LinkedList<>();
        boolean found = false;
        findFirstIsland(grid, n, m, visited, dirs, q, found);
     
        Integer res = countNumberOfZerosToNextIsland(grid, n, m, visited, dirs, q);
        if (res != null) return res;
        return -1;

    }

    private static Integer countNumberOfZerosToNextIsland(int[][] grid, int n, int m, boolean[][] visited, int[][] dirs, Queue<int[]> q) {
        int res = 0;
        while(!q.isEmpty()){
            int size = q.size();
            while(size-- > 0){
                int[] cur = q.poll();
                for(int[] dir : dirs){
                    int x = cur[0] + dir[0];
                    int y = cur[1] + dir[1];
                    if(x < 0 || x >= n || y < 0 || y >= m || visited[x][y]) continue;
                    if(grid[x][y] == 1) return res;
                    visited[x][y] = true;
                    q.add(new int[]{x,y});
                }
            }
            res++;
        }
        return null;
    }

    private void findFirstIsland(int[][] grid, int n, int m, boolean[][] visited, int[][] dirs, Queue<int[]> q, boolean found) {
        for(int i = 0; i < n; i++){
            if(found) break;
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 1){
                    dfs(grid, visited,i,j, dirs, q);
                    found = true;
                    break;
                }
            }
        }
    }

    private void dfs(int[][] grid, boolean[][] visited, int i, int j, int[][] dirs, Queue<int[]> q) {
int n = grid.length;
        int m = grid[0].length;
        if(i < 0 || i >= n || j < 0 || j >= m || visited[i][j] || grid[i][j] == 0) return;
        visited[i][j] = true;
        q.add(new int[]{i,j});
        for(int[] dir : dirs) {
            dfs(grid, visited, i + dir[0], j + dir[1], dirs, q);
        }

    }
}
 