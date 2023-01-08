class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
   double[] res = new double[queries.size()];

        UnionFind uf = new UnionFind();
        for (int i = 0; i < values.length; i++) {
            List<String> equation = equations.get(i);
            uf.union(equation.get(0), equation.get(1), values[i]);
        }

        int idx = 0;
        for (List<String> query : queries) {

            Pair<String, Double> pair0 = uf.find(query.get(0));
            Pair<String, Double> pair1 = uf.find(query.get(1));

            res[idx] = -1d;
            if (pair0 != null && pair1 != null && pair0.getKey().equals(pair1.getKey()))
                res[idx] = pair0.getValue() / pair1.getValue();
            idx++;
        }
        return res;
    }

    public class Pair<T, U> {
        private T key;
        private U val;

        public Pair(T first, U second) {
            this.key = first;
            this.val = second;
        }


        public T getKey() {
            return key;
        }

        public U getValue() {
                return val;
        }
    }
    class UnionFind {
        Map<String, Pair<String, Double>> data = new HashMap<>();

        public Pair<String, Double> find(String x) {
            if (!data.containsKey(x)) return null;//new Pair<>(x, -1d);

            Pair<String, Double> group = data.get(x);

            if (!group.getKey().equals(x)) {
                Pair<String, Double> newGroup = find(group.getKey());
                group = new Pair<>(newGroup.getKey(), group.getValue() * newGroup.getValue());
                data.put(x, group); //update group
            }
            return group;
        }

        public void union(String x, String y, double value){
            if (!data.containsKey(x)) data.put(x, new Pair<>(x, 1d));
            if (!data.containsKey(y)) data.put(y, new Pair<>(y, 1d));

            Pair<String, Double> groupX = find(x);
            Pair<String, Double> groupY = find(y);

            if (groupX.getKey().equals(groupY.getKey())) return;

            Pair<String, Double> pair = new Pair<>(groupY.getKey(), value * groupY.getValue() / groupX.getValue());
            data.put(groupX.getKey(), pair);
        }
    }
}