class Solution {
    public int maxSubarraySumCircular(int[] nums) {
          int maxSum=Integer.MIN_VALUE;
        int globalSum=0;
        int minSum=Integer.MAX_VALUE;
        int globalMinSum=0;
        int arrSum=0;

        for(int n:nums){
            globalSum= Math.max(globalSum+n,n);
            maxSum=Math.max(maxSum,globalSum);
            globalMinSum=Math.min(globalMinSum+n,n);
            minSum=Math.min(minSum,globalMinSum);
            arrSum+=n;
        }

        return maxSum>0?Math.max(maxSum,arrSum-minSum):maxSum;
    }
}