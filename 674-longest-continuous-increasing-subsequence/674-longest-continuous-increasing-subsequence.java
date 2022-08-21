class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int res=0,end=0;
        for(int i=0;i<nums.length;i++){
            if(i>0 && nums[i-1]>=nums[i])end=i;
            res=Math.max(res,i-end+1);
        }
        return res;
    }
}