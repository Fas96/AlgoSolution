class Solution {
    public int numberOfWeakCharacters(int[][] points) {
        
 
    Arrays.sort(points, (a, b)-> (a[0]==b[0]? a[1]-b[1]:a[0]-b[0]));
     
    PriorityQueue<int[]> pqy=new PriorityQueue<>((a, b)-> (a[1]==b[1]? a[0]-b[0]:a[1]-b[1]));
    int ans=0;
    int i=0;
    for(  ;i<points.length;){
        List<int[]> toAdd=new ArrayList(); 
        int x=points[i][0];
        while(i<points.length && points[i][0]==x){
            toAdd.add(points[i]);
            i++;
            
        }
        for(int[] p: toAdd){
            while(!pqy.isEmpty() && pqy.peek()[0]<p[0] && pqy.peek()[1]<p[1]){
                ans++;  
                pqy.poll();
            }
        }
        for(int[] p: toAdd){ 
            pqy.offer(new int[]{p[0], p[1]});
        }
        
    }
    return ans;
}
}