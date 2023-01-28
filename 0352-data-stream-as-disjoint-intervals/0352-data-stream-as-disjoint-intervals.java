//Personal Understanding refactored copy 
class SummaryRanges {

        TreeMap<Integer, Integer> intervals;
        public SummaryRanges() {
            intervals = new TreeMap<>();
        }
        public void addNum(int value) {
            if(isValidInKeys(value)) return;
            extractLowHigh(value);
        }

        private void extractLowHigh(int value) {
            Integer low = intervals.lowerKey(value);
            Integer high = intervals.higherKey(value);
            insertOnConditions(value, low, high);
        }

        private void insertOnConditions(int value, Integer low, Integer high) {
            if(isValidRange(value, low, high)){
                intervals.put(low, intervals.get(high));
                intervals.remove(high);
            } else if(isHigherBoundsMissing(value, low)){
                intervals.put(low, Math.max(intervals.get(low), value));
            } else if(isLowerBoundMissing(value, high)){
                intervals.put(value, intervals.get(high));
                intervals.remove(high);
            } else {
                intervals.put(value, value);
            }
        }

        private boolean isValidInKeys(int value) {
            return intervals.containsKey(value);
        }

        private boolean isHigherBoundsMissing(int value, Integer low) {
            return low != null && intervals.get(low) + 1 >= value;
        }

        private boolean isLowerBoundMissing(int value, Integer high) {
            return high != null && high == value + 1;
        }

        private boolean isValidRange(int value, Integer low, Integer high) {
            return low != null && high != null && intervals.get(low) + 1 == value && high == value + 1;
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