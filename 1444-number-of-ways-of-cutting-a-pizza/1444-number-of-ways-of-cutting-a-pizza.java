class Solution {
 public int ways(String[] pizza, int k) {
        int m = pizza.length;
        int n = pizza[0].length();
       int appleCount[][] = new int[m][n]; 

        //counting the sum of all the apples present in that particular block from (r,c) to (m,n)
       countApple(appleCount, m, n,pizza);
        long mod = (long)1e9+7;

        //a table to keep track that for a particular row column combination with that much number of cuts if the result is already calculated or not. 
        long dp[][][] = new long[m][n][k];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                Arrays.fill(dp[i][j], -1);
            }
        }
       return (int)(solve(0,0, m, n, dp, appleCount, k-1, mod, pizza)%mod);
    }

    private long solve(int i, int j, int m, int n, long dp[][][], int appleCount[][], int k, long mod, String [] pizza){

        //check if our current (r,c) exceeds the input lenght;
        if(i>=m || j>=n){
            return 0;
        }

        //if the block we are traversing has any atleast one apple or not
        if(appleCount[i][j] ==0 ){
            return 0;
        }

        //base case : if all cuts are done and in this last pizza there is atleast one apple.
        if(k==0){
            return 1;
        }

        if(dp[i][j][k]!=-1){
            return dp[i][j][k];
        }
        long total = 0;

        //check for every possible horizontal cut if that cut is possible or not
        for(int r=i+1;r<m;r++){
            if(appleCount[i][j] - appleCount[r][j]>0){
                total += solve(r, j, m, n, dp, appleCount, k-1 ,mod, pizza)%mod;
                total%=mod;
            
            }
        }

        //check for every possible vertical cut if that cut is possible or not
        for(int c=j+1;c<n;c++){
            if(appleCount[i][j]-appleCount[i][c]>0){
                total += solve(i, c, m, n, dp, appleCount, k-1, mod, pizza)%mod;
                total %=mod;
            }
        }

        dp[i][j][k] = total%mod;

        return total%mod;


    }

    private void countApple(int appleCount[][], int m, int n,String pizza[]){
        appleCount[m-1][n-1] = pizza[m-1].charAt(n-1)=='A'?1 : 0;
        for(int i=n-2;i>=0;i--){
            appleCount[m-1][i] = appleCount[m-1][i+1] + isApple(m-1, i, pizza);
        }

        for(int i=m-2;i>=0;i--){
            appleCount[i][n-1] = appleCount[i+1][n-1] + isApple(i,n-1, pizza);
        }
        for(int i=m-2;i>=0;i--){
            for(int j=n-2;j>=0;j--){
                appleCount[i][j] = appleCount[i+1][j] + appleCount[i][j+1] - appleCount[i+1][j+1] + isApple(i,j,pizza);
            }
        }
    }

    private int isApple(int i, int j, String[] pizza){
        return pizza[i].charAt(j)=='A' ? 1 : 0;
    }
}