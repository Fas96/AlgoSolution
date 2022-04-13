class Solution {
    public int[][] generateMatrix(int n) {
        int[][] soln = new int[n][n];
        int t=1;

        for (int l = 0; l < (n + 1) / 2; l++) {
            // from left to right
            for (int j = l; j < n-l; j++) {
                soln[l][j]=t++;
            }
            // from top to down
            for (int j = l+1; j < (n-l); j++) {
                soln[j][n-l-1]=t++;
            }

            // from right to left

            for (int j = l+1; j < (n - l); j++) {
                soln[n-l-1][n-j-1]=t++;
            }

            // from bottom to top
            for (int j = l+1; j < (n - l-1); j++) {
                soln[n-j-1][l]=t++;
            }
        }
        return soln;
    }
}