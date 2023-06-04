class Solution {
    public int findCircleNum(int[][] isConnected) {
        
        int ans=0;
        boolean[] visited=new boolean[isConnected.length];
        for(int i=0;i<isConnected.length;i++){
            if(!visited[i]){
                ans++;
                dfs(isConnected,i,visited);
            }
        }
        return ans;

    }

    private void dfs(int[][] isConnected, int i, boolean[] visited) {
        visited[i]=true;
        for(int j=0;j<isConnected.length;j++){
            if(isConnected[i][j]==1&&!visited[j]){
                dfs(isConnected,j,visited);
            }
        }
    }
}