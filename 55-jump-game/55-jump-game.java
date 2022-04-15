class Solution {
    public boolean canJump(int[] nums) {
        
           int needed =1;
        for(int i = nums.length-2; i>=0; i--){
            if(needed>nums[i]){
                needed++;
            }else {
                needed = 1;
            }
        }
        return needed ==1;
    }
}