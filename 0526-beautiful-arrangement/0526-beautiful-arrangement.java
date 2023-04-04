class Solution {
    int isBeautiful= 0;
    public int countArrangement(int n) {
        boolean []visited= new boolean[n+1];
        bfs(n, visited, 1);
        return isBeautiful;
    }
    public void bfs(int n, boolean []visited, int c){

        if( c > n){ isBeautiful+= 1;return;}
        
        for ( int i= 1; i <= n; i++){
            if ( !visited[i] && ( i % c == 0 || c % i == 0 )){
                visited[i]= true;
                bfs( n, visited, c+1);
                visited[i]= false;
            }
        }
    }
}