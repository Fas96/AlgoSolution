class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
         long  numberOfFixedBoundSubarray=0;
        int n=nums.length;
        int lastMin=-1,lastMax=-1;
        int leftInvalidIdx=-1;

        for (int i = 0; i < n; i++) {
            if(isInRange(nums[i],minK,maxK)){
                lastMin= isMin(minK, nums[i]) ?i:lastMin;
                lastMax= ismax(maxK, nums[i]) ?i:lastMax;
                numberOfFixedBoundSubarray+=Math.max(0,Math.min(lastMin,lastMax)-leftInvalidIdx);
            }else {
                leftInvalidIdx=i;
                lastMin=-1;
                lastMax=-1;
            }

        }
        return numberOfFixedBoundSubarray;
    }

    private  boolean isMin(int minK, int nums) {
        return minK == nums;
    }

    private  boolean ismax(int minK, int nums) {
        return minK == nums;
    }

    private boolean isInRange(int num, int minK, int maxK) {
        return num>=minK && num<=maxK;
    }
}