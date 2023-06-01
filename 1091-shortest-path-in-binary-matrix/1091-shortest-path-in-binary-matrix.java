class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if(grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0},{1,1},{-1,-1},{-1,1},{1,-1}};
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0,0});
        int res = 0;
        Integer res1 = bfs(grid, n, dirs, q, res);
        if (res1 != null) return res1;
        return -1;

    }

    private static Integer bfs(int[][] grid, int n, int[][] dirs, Queue<int[]> q, int res) {
        while(!q.isEmpty()){
            int size = q.size();
            res++;
            while(size-- > 0){
                int[] cur = q.poll();
                int x = cur[0], y = cur[1];
                if(x == n - 1 && y == n - 1) return res;
                dirTraversal(grid, n, dirs, q, x, y);
            }
        }
        return null;
    }

    private static void dirTraversal(int[][] grid, int n, int[][] dirs, Queue<int[]> q, int x, int y) {
        for(int[] dir : dirs){
            int nx = x + dir[0], ny = y + dir[1];
            if(nx < 0 || nx >= n || ny < 0 || ny >= n || grid[nx][ny] == 1) continue;
            grid[nx][ny] = 1;
            q.add(new int[]{nx,ny});
        }
    }
}