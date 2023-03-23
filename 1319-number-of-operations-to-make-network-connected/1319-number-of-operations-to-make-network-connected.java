class Solution {
    public int makeConnected(int n, int[][] connections) {
        DisjointSet s= new DisjointSet(n);
        int connectedEdges=0;
        for (int [] edge:connections) {
            if(!s.union(edge[0],edge[1])) connectedEdges++;
        }
        int count=0;
        for(int i = 0; i<n; i++){
            if(s.find(i) == i) count++;
        }
        return connectedEdges>=(count-1)?(count-1):-1;
    }
    public class DisjointSet {
        List<Integer> parent = new ArrayList<>();
        List<Integer> size = new ArrayList<>();

        public DisjointSet(int n) {
            for(int i = 0; i<=n; i++){
                parent.add(i);
                size.add(1);
            }
        }
         public int find(int x) {
             if(x==parent.get(x))return x;
             int xx=find(parent.get(x));
             parent.set(x,xx);
             return parent.get(x);
        }


        public boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX==rootY) return false;
            if(size.get(rootX) < size.get(rootY)){
                parent.set(rootX, rootY);
                size.set(rootY, size.get(rootY)+size.get(rootX));
                return true;
            }else{
                parent.set(rootY, rootX);
                size.set(rootX, size.get(rootY)+size.get(rootX));
                return true;
            }
        }
    }
}