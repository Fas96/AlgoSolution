class Solution {
   public int longestConsecutive(int[] nums) {
        int n=nums.length;
        if(n==0)return 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int counter = 0;
        for (int num : nums) {
            if (map.containsKey(num))continue;
            map.put(num,counter);
            counter++;
        }
        UF uf = new UF(map.size());
        for (int i: nums){
            uf.union(map.get(i), map.getOrDefault(i-1, -1));
            uf.union(map.get(i), map.getOrDefault(i+1, -1));
        }

        return uf.getMax();
    }

    class UF{
          int[] parents;
        int[] ranks;

        public UF(int n) {
            parents = new int[n];
            ranks = new int[n];
            for(int i = 0; i < n; i++) {parents[i] = i;ranks[i]=1;}
        }

        private int find(int x) {
            if(x != parents[x]) x = find(parents[x]);
            return parents[x];
        }

        private void union(int x, int y) {
            if ((x == -1) || (y == -1)) return ;
            int rootA = find(x);
            int rootB = find(y);
            if(rootB == rootA) return ;
            if (ranks[rootA] < ranks[rootB]){
                ranks[rootB] += ranks[rootA];
                parents[rootA] = rootB;
            } else {
                ranks[rootA] += ranks[rootB];
                parents[rootB] = rootA;
            }

        }
        public int getMax(){
            int max = ranks[0];
            for (int i=1;i<ranks.length;i++)
                max = Math.max(max, ranks[i]);
            return max;
        }
    }
}