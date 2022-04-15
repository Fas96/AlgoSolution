class Solution {
    public int maxSubArray(int[] nums) {
           if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        int maxSum=nums[0];
        
        int usm=0;
        for (int i = 0; i < nums.length; i++) {
            usm+=nums[i];
            if(usm>maxSum){maxSum=usm;}
            if(usm<0)usm=0;
        }



        return maxSum;
    }
}