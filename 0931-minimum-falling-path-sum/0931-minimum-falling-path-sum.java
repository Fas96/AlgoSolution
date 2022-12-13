class Solution {
    public int minFallingPathSum(int[][] grid) {
        //adding extension for OBE
        int[][] dp=new int[grid.length][grid[0].length + 2];
        int n=grid.length;
        if (grid.length == 1)
            return grid[0][0];  

         //the OBE Default set
        for (int i = 0; i < n; i++) {
            dp[i][0] = (int) Math.pow(10, 7);
        }
        for (int i = 0; i < n; i++) {
            dp[i][n + 1] = (int) Math.pow(10, 7);
        }

        int ans = 0;

        for (int i = n - 1; i >= 0; i--) {
            int min = Integer.MAX_VALUE;
            for (int j = 1; j <= n; j++) {
                if (i == n - 1) {
                    dp[i][j] = grid[i][j - 1]; // filling elements of last row of dp array (apart from cusion elements) with values same as those of grid's last row
                } else {

                    int x = grid[i][j - 1] + dp[i + 1][j];  
                    int y = grid[i][j - 1] + dp[i + 1][j - 1];  
                    int z = grid[i][j - 1] + dp[i + 1][j + 1]; 

                    dp[i][j] = Math.min(z, Math.min(y, x));  
                    min = Math.min(min, dp[i][j]); 
                }
            }
            ans = min;
        }
        return ans;
    }
}