class Solution {
    public int jump(int[] nums) {
           int minJump = 0;
        int left=0 , right = 0;
        while(right< (nums.length-1)) {
            int max = 0;

            for(int j = left ; j< right+1 ; j++){
                max = Math.max(max,j+nums[j]);
            }
            left = right + 1;
            right = max;
            minJump++;
        }
        return minJump; 
    }
}