class Solution {
    public int maxSubArray(int[] nums) {
          int maxSum=Integer.MIN_VALUE;
        int globalSum=0;

        for (int x : nums) {
            globalSum=Math.max(globalSum+x,x);
            maxSum=Math.max(maxSum,globalSum);
        }

        return maxSum;
    }
}