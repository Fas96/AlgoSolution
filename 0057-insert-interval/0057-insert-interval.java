class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        
   
        if(intervals==null||intervals.length==0) return new int[][]{newInterval};
        if(newInterval==null) return intervals;
        
        List<Interval> interVals=new ArrayList<>();
        for(int[] interval:intervals){
            interVals.add(new Interval(interval[0],interval[1]));
        }
        interVals.add(new Interval(newInterval[0],newInterval[1]));
        Collections.sort(interVals,(a, b)->Integer.compare(a.start,b.start));
        
        List<Interval> mergedIntervals=new ArrayList<>();
        Interval interval=interVals.get(0);
        int start=interval.start,end=interval.end;
        
        for(int i=1;i<interVals.size();i++){
            interval=interVals.get(i);
            if(interval.start<=end){
                end=Math.max(interval.end,end);
            }else{
                mergedIntervals.add(new Interval(start,end));
                start=interval.start;
                end=interval.end;
            }
        }
        mergedIntervals.add(new Interval(start,end));
        int[][] result=new int[mergedIntervals.size()][2];
        for(int i=0;i<mergedIntervals.size();i++){
            result[i][0]=mergedIntervals.get(i).start;
            result[i][1]=mergedIntervals.get(i).end;
        }
        return result;
         
        

    }
    class Interval{
        int start,end;
        public Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}