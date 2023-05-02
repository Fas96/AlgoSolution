class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
      int ans=0;
        for (int i = 0; i < n; i++) {
            if(informTime[i]==0) ans=Math.max(ans,dfs(i,manager,informTime));
        }
        return ans;
    }

    private int dfs(int idx, int[] manager, int[] informTime) {
        if(manager[idx]==-1)return 0;
        return informTime[manager[idx]]+dfs(manager[idx],manager,informTime);
    }
}