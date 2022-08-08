class Solution {
    public int lengthOfLIS(int[] nums) {
    int[] dp = new int[nums.length];
    int len = 0;  
 
    for(int num: nums){
        int idx = Arrays.binarySearch(dp, 0, len, num);
        if(idx < 0){
            idx = - (idx + 1);
        }
 
        dp[idx] = num; 
        if(idx==len){
            len++;
        }
    }
 
    return len;
    }
}