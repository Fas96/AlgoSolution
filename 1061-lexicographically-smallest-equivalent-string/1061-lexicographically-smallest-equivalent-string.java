class Solution {
   public String smallestEquivalentString(String a, String b, String c) {
        UnionFind uf = new UnionFind(26);
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < a.length(); i++) uf.union(a.charAt(i) - 'a', b.charAt(i) - 'a');
        Map<Integer, Set<Integer>> groupByParent = uf.getGroupsByParent(true);
        for (int i = 0; i < c.length(); i++) {
            int parent = uf.find(c.charAt(i) - 'a');
            TreeSet<Integer> group = (TreeSet<Integer>) groupByParent.get(parent);
            ans.append((char) ('a' + group.first()));
        }
        return ans.toString();

    }

    public class UnionFind {
        private final Map<Integer, Integer> parents, groupSizes;
        private int numGroups, size;

        public UnionFind(int numVertices) {
            parents = new HashMap<>();
            groupSizes = new HashMap<>();
            for (int i = 0; i < numVertices; i++) {
                parents.put(i, i);
                groupSizes.put(i, 1);
            }
            size = numGroups = numVertices;
        }
        public Map<Integer, Set<Integer>> getGroupsByParent(boolean sorted) {
            Map<Integer, Set<Integer>> groups = new HashMap<>();
            for (int i = 0; i < size; i++) {
                int parent = find(i);
                if (!groups.containsKey(parent)) groups.put(parent, sorted ? new TreeSet<>() : new HashSet<>());
                groups.get(parent).add(i);
            }
            return groups;
        }

        public int find(int vertex) {
            if (parents.get(vertex) == vertex) return vertex;
            int parent = find(parents.get(vertex));
            parents.put(vertex, parent); //path compression
            return parent;
        }

        public boolean union(int vertex, int otherVertex) {
            int vertexParent = find(vertex);
            int otherVertexParent = find(otherVertex);
            if (vertexParent == otherVertexParent) return true;

            int vertexGroupSize = groupSizes.get(vertexParent);
            int otherVertexGroupSize = groupSizes.get(otherVertexParent);
            int deadParent = vertexParent;
            int finalParent = otherVertexParent;
            if (vertexGroupSize > otherVertexGroupSize) {
                deadParent = otherVertexParent;
                finalParent = vertexParent;
            }
            parents.put(deadParent, finalParent);
            groupSizes.remove(deadParent);
            groupSizes.put(finalParent, vertexGroupSize + otherVertexGroupSize);
            numGroups--;
            return find(vertex) == find(otherVertex);
        }
    }
}
 

// h,w
// e,o
// l,r
// l,l
// o,d

// h,w
// e,o,d
// l,r

// hdld