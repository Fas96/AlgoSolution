class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        
   int n = edges.length;
        UF uf = new UF(n + 1);
        int[] parent = new int[n + 1];
        int[] candA = null, candB = null;
        for(int[] edge: edges) {
            if(parent[edge[1]] == 0) {
                parent[edge[1]] = edge[0];
            } else {
                candA = new int[]{parent[edge[1]], edge[1]};
                candB = new int[]{edge[0], edge[1]};
                edge[1] = 0;
            }
        }
        for(int[] edge: edges) {
            if(edge[1] == 0) continue;
            if(!uf.union(edge[0], edge[1])) {
                if(candA == null) return edge;
                return candA;
            }
        }
        return candB;
        

    }
    class UF{
        int[] parents;
        int[] ranks;

        public UF(int n) {
            parents = new int[n];
            ranks = new int[n];
            for(int i = 0; i < n; i++) parents[i] = i;
        }

        private int find(int x) {
            if(x != parents[x]) x = find(parents[x]);
            return parents[x];
        }

        private boolean union(int x, int y) {
            int px = find(x);
            int py = find(y);
            if(px == py) return false;
            if(ranks[px] > ranks[py]) {
                parents[py] = px;
                ranks[px] ++;
            } else{
                parents[px] = py;
                ranks[py] ++;
            }
            return true;
        }
    }
}