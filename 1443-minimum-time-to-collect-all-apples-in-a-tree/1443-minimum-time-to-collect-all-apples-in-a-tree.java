class Solution {
    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
      List<List<Integer>> graph = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                graph.add(new ArrayList<>());
            }
            for (int[] edge : edges) {
                graph.get(edge[0]).add(edge[1]);
                graph.get(edge[1]).add(edge[0]);
            }
        boolean[] visited = new boolean[n];
        return dfs(0,hasApple,graph,visited);

    }

    private int dfs(int node, List<Boolean> hasApple, List<List<Integer>> graph, boolean[] visited) {
        
         if(visited[node]) return 0;
        visited[node] = true; 
        int sum = 0;
        for(int edge : graph.get(node))
        {
            sum += dfs(edge, hasApple, graph, visited);
        } 
        if(node==0) return  sum;  
        if(hasApple.get(node) || sum>0 ) return (2 + sum);
 
        else return 0;
    }
}