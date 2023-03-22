
import java.util.*;
class Solution {
     public int minScore(int n, int[][] roads) {
        UF u=new UF(n+1);
        for (int[] road : roads) u.union(road[0],road[1],road[2]);
        return (u.find(1)==u.find(n))?u.distance[u.find(1)]:-1;
    }


    public class UF {
        private int[] group;
        private int[] rank;
        private int[] distance;
        public int find(int x) {
            return x == group[x] ? x: (group[x] = find(group[x]));
        }
        public void union(int x, int y, int d){
            int rootX = find(x);
            int rootY = find(y);

            int minD = Math.min(distance[rootX], distance[rootY]);
            minD = Math.min(minD, d);
            distance[rootX] = distance[rootY] = minD;

            if (rootX == rootY) return;
            if (rank[rootX] < rank[rootY]){
                group[rootX] = rootY;
            }else{
                group[rootY] = rootX;
                if (rank[rootX] == rank[rootY]) rank[rootX]++;
            }
        }
        public UF(int size) {
            group = new int[size];
            rank = new int[size];
            distance = new int[size];
            for (int i = 0; i < size; i++) {
                group[i] = i;
                rank[i] = 1;
                distance[i] = Integer.MAX_VALUE;
            }

        }
    }

}
 