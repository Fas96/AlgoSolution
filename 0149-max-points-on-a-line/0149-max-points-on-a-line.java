class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n < 3) return n;
        int maxEqualGradientCount = 0;
       
        for (int [] curXYPlane: points){
            Map<Double, Integer> gradientCountMap = new TreeMap<>();
            for (int[] cur: points) {
                if (curXYPlane[0] == cur[0] && curXYPlane[1] == cur[1]) continue;
                double gradient = (curXYPlane[0] == cur[0]) ? Double.MAX_VALUE : (double) (curXYPlane[1] - cur[1]) / (curXYPlane[0] - cur[0]);
                gradientCountMap.put(gradient, gradientCountMap.getOrDefault(gradient, 0) + 1);
            }
            
            int curMaxEqualGradient = gradientCountMap.values().stream().mapToInt(Integer::intValue).max().orElse(0);
             maxEqualGradientCount = Math.max(maxEqualGradientCount, curMaxEqualGradient!=0? curMaxEqualGradient + 1: 0);
        }
        return maxEqualGradientCount;
    }
}