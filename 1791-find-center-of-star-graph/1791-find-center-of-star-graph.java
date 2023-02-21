class Solution {
    public int findCenter(int[][] edges) {
         Set<Integer> components = new HashSet<>();
        Map<Integer, LinkedList<Integer>> map = new HashMap<>();
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            components.add(u);
            components.add(v);
            map.putIfAbsent(u, new LinkedList<>());
            map.putIfAbsent(v, new LinkedList<>());
            map.get(u).add(v);
            map.get(v).add(u);
        }
        int center = -1;
        for (int component : components) {
            if (map.get(component).size() == components.size() - 1) {
                center = component;
                break;
            }
        }
        return center;
    }
}