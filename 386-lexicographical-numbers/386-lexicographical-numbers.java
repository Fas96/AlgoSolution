class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i <= 9; i++) {
            dfs(i, n, ans);
        }
        return ans;
    }

    private void dfs(int i, int n, List<Integer> ans) {
        if (i > n) return;
        ans.add(i);
        for (int j = 0; j <= 9; j++) {
            dfs(i * 10 + j, n, ans);
        }
    }
}