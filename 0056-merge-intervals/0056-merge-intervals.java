class Solution {
    public int[][] merge(int[][] intervals) {
        List<InterVal> interVals=new ArrayList<>();
        for(int[] interval:intervals){
            interVals.add(new InterVal(interval[0],interval[1]));
        }
        Collections.sort(interVals,(a, b)->Integer.compare(a.start,b.start));
        
        List<InterVal> mergedIntervals=new ArrayList<>();
        
        InterVal interval=interVals.get(0);
        int start=interval.start,end=interval.end;
        
        for(int i=1;i<interVals.size();i++){
            interval=interVals.get(i);
            if(interval.start<=end){
                end=Math.max(interval.end,end);
            }else{
                mergedIntervals.add(new InterVal(start,end));
                start=interval.start;
                end=interval.end;
            }
        }
        mergedIntervals.add(new InterVal(start,end));
        
        int[][] result=new int[mergedIntervals.size()][2];
        
        for(int i=0;i<mergedIntervals.size();i++){
            result[i][0]=mergedIntervals.get(i).start;
            result[i][1]=mergedIntervals.get(i).end;
        }
        return result;
    }
    class InterVal{
        int start,end;
        public InterVal(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}