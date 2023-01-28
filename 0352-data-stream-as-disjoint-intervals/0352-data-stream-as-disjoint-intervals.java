 class SummaryRanges {
        TreeMap<Integer, Integer> intervals;
        public SummaryRanges() {
            intervals = new TreeMap<>();
        }
        public void addNum(int value) {
            if(intervals.containsKey(value)) return;
            Integer low = intervals.lowerKey(value);
            Integer high = intervals.higherKey(value);
            if(low != null && high != null && intervals.get(low) + 1 == value && high == value + 1){
                intervals.put(low, intervals.get(high));
                intervals.remove(high);
            } else if(low != null && intervals.get(low) + 1 >= value){
                intervals.put(low, Math.max(intervals.get(low), value));
            } else if(high != null && high == value + 1){
                intervals.put(value, intervals.get(high));
                intervals.remove(high);
            } else {
                intervals.put(value, value);
            }
        }

        public int[][] getIntervals() {
            int[][] res = new int[intervals.size()][2];
            int i = 0;
            for(int key : intervals.keySet()){
                res[i][0] = key;
                res[i][1] = intervals.get(key);
                i++;
            }
            return res;

        }
    }