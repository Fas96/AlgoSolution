class Solution {
 public int bagOfTokensScore(int[] t, int p) {
        Arrays.sort(t);
        return helper(t, 0, t.length-1, p, 0);
    }
    private int helper(int[] t, int i, int j, int p, int points){
        if(i > j) return points;
        int max = points;
        if(t[i] <= p)
            max = Math.max(max, helper(t, i+1, j, p-t[i], points+1));
        else if(points >= 1)
            max = Math.max(max, helper(t, i, j-1, p+t[j], points-1));
        return max;
    }
}