
import java.util.*;
class Solution {
       public int minScore(int n, int[][] roads) {
        List<List<Pair<Integer, Integer>>> graph = new ArrayList<>();
        for(int i = 0;i<=n;i++) graph.add(new ArrayList<Pair<Integer, Integer>>());
        
        for(int[] road: roads) {
            graph.get(road[0]).add(new Pair(road[1], road[2]));
            graph.get(road[1]).add(new Pair(road[0], road[2]));
        }
        
        boolean[] vis = new boolean[n+1]; 
        return dfs(graph, vis, 1);
    }
    
    public int dfs(List<List<Pair<Integer, Integer>>> graph, boolean[] vis, int root) {
        vis[root] = true;
        int ans = Integer.MAX_VALUE;
        for(Pair<Integer, Integer> edge:  graph.get(root)) {
            ans = Math.min(ans, edge.getValue());
            if(!vis[edge.getKey()]) {
                ans = Math.min(ans, dfs(graph, vis, edge.getKey()));
            }
        }
        
        return ans;
    }
}
 