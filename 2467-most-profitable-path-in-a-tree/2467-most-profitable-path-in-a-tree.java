class Solution {
   public int mostProfitablePath(int[][] edges, int bob, int[] amount) {
        Map<Integer, List<Integer>> graph = buildGraph(edges);
        int[] bobTimestamps = new int[graph.size()];
        goBob(graph, bob, -1, 1, bobTimestamps);
        return goAlice(graph, 0, -1, 1, bobTimestamps, amount);
    }

    Map<Integer, List<Integer>> buildGraph(int[][] edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new LinkedList<>()).add(edge[1]);
            graph.computeIfAbsent(edge[1], k -> new LinkedList<>()).add(edge[0]);
        }
        return graph;
    }

    boolean goBob(Map<Integer, List<Integer>> graph, int bob, int prev, int time, int[] bobTimestamps) {
        bobTimestamps[bob] = time;
        if (bob == 0) { return true; }
        for (int next : graph.get(bob)) {
            if (next == prev) { continue; }
            if (goBob(graph, next, bob, time + 1, bobTimestamps)) {
                return true;
            }
        }
        bobTimestamps[bob] = 0;
        return false;
    }

    int goAlice(Map<Integer, List<Integer>> graph, int alice, int prev, int time, int[] bobTimestamps, int[] amount) {
        int max = Integer.MIN_VALUE;
        for (int next : graph.get(alice)) {
            if (next == prev) { continue; }
            max = Math.max(max, goAlice(graph, next, alice, time + 1, bobTimestamps, amount));
        }

        int reward = (time < bobTimestamps[alice] || bobTimestamps[alice] == 0)
                ? amount[alice]
                : time == bobTimestamps[alice]
                ? amount[alice] / 2
                : 0;
        return (max == Integer.MIN_VALUE ? 0 : max) + reward;
    }
}