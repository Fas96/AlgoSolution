class Solution {
    public int[][] updateMatrix(int[][] mat) {
          int m = mat.length, n = mat[0].length;
        int[][] res = new int[m][n];
         //bfs
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    q.offer(new int[]{i, j});
                } else {
                    res[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int[] dir : dirs) {
                int x = cur[0] + dir[0], y = cur[1] + dir[1]; 
                if (x < 0 || x >= m || y < 0 || y >= n)continue;  
                if(res[x][y] <= res[cur[0]][cur[1]] + 1) continue;
                res[x][y] = res[cur[0]][cur[1]] + 1;
                q.offer(new int[]{x, y});
            }
        }
        
        
        return res;
    }
}