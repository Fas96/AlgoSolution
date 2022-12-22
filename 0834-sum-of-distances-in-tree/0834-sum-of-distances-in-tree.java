class Solution {
    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        
   if (n == 1) return new int[]{0};
        
        Map<Integer, LinkedList<Integer>> map = new HashMap<>();
        for (int[] edge : edges) {
            map.computeIfAbsent(edge[0], f -> new LinkedList<>()).add(edge[1]);
            map.computeIfAbsent(edge[1], f -> new LinkedList<>()).add(edge[0]);
        } 
        
        int[] count = new int[n];
        int[] dist = new int[n];
        dfs(map, count, dist, 0, -1);
        dfs2(map, count, dist, 0, -1, n);
        return dist; 

    }

    private void dfs2(Map<Integer, LinkedList<Integer>> map, int[] count, int[] dist, int i, int i1, int n) {
        for (int j : map.get(i)) {
            if (j == i1) continue;
            dist[j] = dist[i] - count[j] + n - count[j];
            dfs2(map, count, dist, j, i, n);
        }
    }

    private void dfs(Map<Integer, LinkedList<Integer>> map, int[] count, int[] dist, int i, int i1) {
        for (int j : map.get(i)) {
            if (j == i1) continue;
            dfs(map, count, dist, j, i);
            count[i] += count[j];
            dist[i] += dist[j] + count[j];
        }
        count[i]++;
    }
}