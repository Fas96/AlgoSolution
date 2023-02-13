class Solution {
    public int minOperations(int[] nums) {
         int n= nums.length;
        int ans=0;
        for (int i = 1; i < n; i++) {
            if(nums[i-1]>=nums[i]){
                ans+=nums[i-1]-nums[i]+1;
                nums[i]=nums[i-1]+1;
            }
        }
        return ans;
    }
}

 