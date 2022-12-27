class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
           int n = capacity.length;
        int[] deficiency = new int[n];
        int totalDeficiency = 0;
        for (int i = 0; i < n; i++) {
            deficiency[i] = capacity[i] - rocks[i];
        }
        Arrays.sort(deficiency);

        while (totalDeficiency < n && additionalRocks >= deficiency[totalDeficiency]) {
            additionalRocks -= deficiency[totalDeficiency];
            totalDeficiency++;
        }
        return totalDeficiency;
    }
}