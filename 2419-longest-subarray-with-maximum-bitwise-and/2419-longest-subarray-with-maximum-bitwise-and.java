class Solution {
    public int longestSubarray(int[] nums) {
        int getMax= Arrays.stream(nums).max().getAsInt();
        int ans=0;
        int mx=Integer.MIN_VALUE;
        for (int num : nums) {
            if(num==getMax)ans++;
            else{
                mx=Math.max(ans,mx);
                ans=0;
            }
        }
        
        return  Math.max(mx,ans);
    }
}