class Solution {
   public boolean validPath(int n, int[][] edges, int source, int destination) {
          HashMap<Integer, Stack<Integer>> graph = new HashMap<>();
        boolean[] visited = new boolean[n];
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new Stack<>()).push(edge[1]);
            graph.computeIfAbsent(edge[1], k -> new Stack<>()).push(edge[0]);
        }
        return dfs(graph, visited, source, destination);

    }

    private boolean dfs(HashMap<Integer, Stack<Integer>> graph, boolean[] visited, int source, int destination) {
        if (source == destination) {
            return true;
        }
        visited[source] = true;
        for (Integer next : graph.getOrDefault(source, new Stack<>())) {
            if (!visited[next]) {
                if (dfs(graph, visited, next, destination)) {
                    return true;
                }
            }
        }
        return false;
    }
}