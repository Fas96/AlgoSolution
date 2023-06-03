class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        int ans=Integer.MIN_VALUE;

        for (int idx = 0; idx < n; idx++) {
            //inform time is 0 for
            if(informTime[idx]==0) ans=Math.max(ans,dfs(idx,manager,informTime));
        }
        return ans;
    }

    private int dfs(int idx, int[] manager, int[] informTime) {
        if(manager[idx]==-1)return 0;
        return informTime[manager[idx]]+dfs(manager[idx],manager,informTime);
    }
}