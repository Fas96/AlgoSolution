class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        
   Map<String,Map<String,Double>> mapValuePairs= new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            String x=equations.get(i).get(0);
            String y=equations.get(i).get(1);
            mapValuePairs.putIfAbsent(x, new HashMap<>());
            mapValuePairs.get(x).put(y,values[i]);
            mapValuePairs.putIfAbsent(y, new HashMap<>());
            mapValuePairs.get(y).put(x,1/values[i]);
        }
        int QN=queries.size();
        double[] answer= new double[QN];
        for (int i = 0; i < QN; i++) {
            answer[i]=dfs(queries.get(i).get(0) , queries.get(i).get(1) , new HashSet<>(), mapValuePairs);

        }
        return  answer;
    }
    public double dfs(String src, String dest, Set<String> visited, Map<String, Map<String, Double>> graph) {
        if(!graph.containsKey(src)) return -1.0;
        if(graph.get(src).containsKey(dest)) return graph.get(src).get(dest);

        visited.add(src);
        for(Map.Entry<String, Double> nbr : graph.get(src).entrySet()){
            if(!visited.contains(nbr.getKey())){
                double weight = dfs(nbr.getKey(), dest, visited, graph);
                if(weight != -1.0){
                    return nbr.getValue() * weight;
                }
            }
        }
        return -1.0;
    }
}