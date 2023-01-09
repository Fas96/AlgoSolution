class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        
  int n = edges.length;
        UF uf = new UF(n + 1);
        for(int[] edge: edges) {
            if(!uf.union(edge[0], edge[1])) return edge;
        }
        return new int[0];
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