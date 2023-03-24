class Solution {
    public int minReorder(int n, int[][] connections) { 
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] connection : connections) {
            //add the edge from parent to child
            graph[connection[0]].add(connection[1]);
            //change the direction of the edge from child to parent
            graph[connection[1]].add(-connection[0]);
        }
        return dfs(graph, 0, new boolean[n]);
    }

    private int dfs(List<Integer>[] graph, int from, boolean[] booleans) {
        booleans[from] = true;
        int ans = 0;
        for (int to : graph[from]) {
            if (booleans[Math.abs(to)]) continue;
            ans += to > 0 ? 1 : 0;
            ans += dfs(graph, Math.abs(to), booleans);
        }
        return ans;
    }
}