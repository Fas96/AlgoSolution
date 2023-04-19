class Solution {
    public int minSubArrayLen(int target, int[] nums) {
         int windowSum=0;
        int minLen=Integer.MAX_VALUE;
        int windowStart=0;
        for (int windowEnd = 0; windowEnd < nums.length; windowEnd++) {
            windowSum+=nums[windowEnd];
            while (windowSum>=target){
                minLen=Math.min(minLen,windowEnd-windowStart+1);
                windowSum-=nums[windowStart];
                windowStart++;
            }
        }
        return (minLen==Integer.MAX_VALUE)?0:minLen;
    }
}