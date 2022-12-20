class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
      int[] parent = new int[rooms.size()];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }

        Set<Integer> v = new HashSet<>();
        Queue<List<Integer>> keys = new LinkedList<>();
        keys.add(rooms.get(0));
        v.add(0);

        while (!keys.isEmpty()) {
            List<Integer> temp = keys.poll();
            for (int i = 0; i < temp.size(); i++) {

                int x = find(parent, temp.get(i));

                int y = find(parent, 0);

                if (x != y) {
                    union(parent, x, y);
                }
                if (!v.contains(temp.get(i))) {
                    v.add(temp.get(i));
                    keys.add(rooms.get(temp.get(i)));
                }
            }
        }

 
        int x = find(parent, 0);
                for (int i = 1; i < parent.length; i++) {
                    if (find(parent, i) != x) {
                        return false;
                    }
                }
                return true;
            }
    
        int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
        }

 
        void union(int[] parent, int x, int y) {
            int xRoot = find(parent, x);
            int yRoot = find(parent, y);
            if (xRoot != yRoot) {
                parent[xRoot] = yRoot;
            }
        }
}