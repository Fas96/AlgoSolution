class Solution {
    public int findMinArrowShots(int[][] points) {
        //common template for overlapping ends
        int numberOfOverlappingEnds = 0;
        int minimumEnd = Integer.MAX_VALUE;
        
        Arrays.sort(points, Comparator.comparingInt(o -> o[1]));
        
        for (int[] p : points) {
            
            if (p[0] > minimumEnd) {
                numberOfOverlappingEnds++;
                minimumEnd = p[1];
            } else {
                minimumEnd = Math.min(minimumEnd, p[1]);
            }
        }
        return numberOfOverlappingEnds + (points.length > 0 ? 1 : 0);

    }
}