class Solution {
    public int[][] generateMatrix(int n) {
     
        int [] [] matrix = new int[n][n];
        int rowStart = 0, rowEnd = n-1, colStart = 0, colEnd = n-1;
        int total = n*n;
        int start=1;
        while (start<=total) {
            for (int i = colStart; i <= colEnd; i++) {
                matrix[rowStart][i]=start;
                start++;
            }
            rowStart++;
            for (int i = rowStart; i <= rowEnd; i++) {
                matrix[i][colEnd]=start;
                start++;
            }
            colEnd--;
            if (rowStart <= rowEnd) {
                for (int i = colEnd; i >= colStart; i--){
                    matrix[rowEnd][i]=start;
                    start++;
                }
                rowEnd--;
            }
            if (colStart <= colEnd) {
                for (int i = rowEnd; i >= rowStart; i--)
                { matrix[i][colStart]=start;start++;}
                colStart++;
            }
        }
       return matrix;
    }
}