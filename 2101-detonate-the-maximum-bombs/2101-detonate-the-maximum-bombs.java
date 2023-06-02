class Solution {
    public int maximumDetonation(int[][] bombs) {
        int n = bombs.length;
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
            for(int j = 0; j < n; j++) {
                if(i == j) continue; 
                if((new Circle(bombs[i][0], bombs[i][1], bombs[i][2])).canDetonate(new Circle(bombs[j][0], bombs[j][1], bombs[j][2]))) {
                    graph.get(i).add(j);
                }
            }
        }

        int max = 0;
        for(int i = 0; i < n; i++) {
            max = Math.max(max, dfs(graph, new boolean[n], i));
        }

        return max;
    }

    private int dfs(List<List<Integer>> graph, boolean[] vis, int src) {
        vis[src] = true;
        int res = 1;
        for(int next: graph.get(src)) {
            if(vis[next]) continue;
            res += dfs(graph, vis, next);
        }
        return res;
    } 
    class Circle {
        int x;
        int y;
        int r;
        public Circle(int x, int y, int r) {
            this.x = x;
            this.y = y;
            this.r = r;
        }
        
        public boolean canDetonate(Circle other) {
            double dist = Math.sqrt(Math.pow(other.y - this.y, 2) + Math.pow(other.x - this.x, 2));
            return this.r >= dist;
        }
    }
}