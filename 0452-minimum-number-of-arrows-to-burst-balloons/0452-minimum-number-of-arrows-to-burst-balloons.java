class Solution {
    public int findMinArrowShots(int[][] points) {
        
        int count = 0, minEnd = Integer.MAX_VALUE;
        Arrays.sort(points, Comparator.comparingInt(o -> o[1]));
        for (int[] p : points) {
            
            if (p[0] > minEnd) {
                count++;
                minEnd = p[1];
            } else {
                minEnd = Math.min(minEnd, p[1]);
            }
        }
        return count + (points.length > 0 ? 1 : 0);

    }
}