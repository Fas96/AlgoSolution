class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        boolean[] visited = new boolean[n];
        double[] maxProb = new double[n];
        maxProb[start] = 1.0;
        
        while(true){
            int maxProbNode = -1;
            for(int i=0; i<n; i++){
                if(!visited[i] && (maxProbNode==-1 || maxProb[i]>maxProb[maxProbNode])){
                    maxProbNode = i;
                }
            }
            if(maxProbNode==-1 || maxProbNode==end){
                break;
            }
            visited[maxProbNode] = true;
            for(int i=0; i<edges.length; i++){
                if(edges[i][0]==maxProbNode){
                    maxProb[edges[i][1]] = Math.max(maxProb[edges[i][1]], maxProb[maxProbNode]*succProb[i]);
                }
                if(edges[i][1]==maxProbNode){
                    maxProb[edges[i][0]] = Math.max(maxProb[edges[i][0]], maxProb[maxProbNode]*succProb[i]);
                }
            }
        }
        return maxProb[end]; 
    }
}