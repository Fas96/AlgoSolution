class Solution {
    public int rob(int[] nums) {
         int n=nums.length;
        int[] prevD=new int[n];
        prevD[0]=nums[0];
        for (int i = 1; i <n; i++) {
            if(i>=2){
                prevD[i]=Math.max(prevD[i],Math.max(nums[i]+prevD[i-2],prevD[i-1] ));
            }else{
                prevD[i]=Math.max(nums[i],prevD[i-1]);
            }
        }
        return prevD[n-1];
    }
}