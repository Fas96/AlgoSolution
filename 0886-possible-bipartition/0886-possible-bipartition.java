class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        UF_BOP uf = new UF_BOP(n);
        HashMap<Integer, LinkedList<Integer>> disMap = new HashMap<>();

        for(int[] d: dislikes) {
            int x = d[0], y = d[1];
            disMap.computeIfAbsent(x, f -> new LinkedList<>()).add(y);
            disMap.computeIfAbsent(y, f -> new LinkedList<>()).add(x);
        }


        for(int i = 1; i <= n; i++) {
            if (disMap.get(i) != null) {
                int initDisLike = disMap.get(i).get(0);
                for (int j = 1; j < disMap.get(i).size(); j++) {
                    int dis = disMap.get(i).get(j);
                    if (!uf.union(initDisLike, dis, i)) return false;
                }
            }
        }
        return true;





    }

    class UF_BOP {
        private int[] parents;
        public UF_BOP(int n) {
            parents = new int[n + 1];
            for(int i = 1; i <= n; i++) {
                parents[i] = i;
            }
        }
        public int find(int x) {
            if(parents[x] == x) return x;
            return parents[x] = find(parents[x]);
        }
        public boolean union(int x, int y, int parent) {
            int rX = find(x);
            parents[y] = rX;
            return rX != find(parent);
        }
    }
}
 

 