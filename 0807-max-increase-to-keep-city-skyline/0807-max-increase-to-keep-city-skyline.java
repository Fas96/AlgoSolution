class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
       int M = grid.length;
        int N= grid[0].length;
        long differences=0;
        int[] keepMaxOfROW = new int[grid.length];
        int[] keepMaxOfCOL = new int[grid[0].length];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                keepMaxOfROW[i] = Math.max(keepMaxOfROW[i], grid[i][j]);
                keepMaxOfCOL[j] = Math.max(keepMaxOfCOL[j], grid[i][j]);
            }
        }

    
      

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                differences += Math.min(keepMaxOfROW[i], keepMaxOfCOL[j]) - grid[i][j]; 
            }
        }
        
        return (int) differences;
    }
    
}