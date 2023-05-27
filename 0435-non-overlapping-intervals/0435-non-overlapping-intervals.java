class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int count=0;
        if(intervals==null||intervals.length==0)return count;
        Arrays.sort(intervals,(a, b)->Integer.compare(a[0],b[0]));
        int end=intervals[0][1];
        for(int i=1;i<intervals.length;i++){
            if(intervals[i][0]<end){
                count++;
                end=Math.min(end,intervals[i][1]);
            }else{
                end=intervals[i][1];
            }
        }
        return count;
    }
}