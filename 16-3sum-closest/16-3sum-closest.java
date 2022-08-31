class Solution {
    public int threeSumClosest(int[] nums, int target) {
       //base case
        int gap= Integer.MAX_VALUE,ans=0;
        if(nums.length<3)return 0;
        Arrays.sort(nums);
        int n=nums.length;
        for (int i = 0; i < n; i++) {
            int L=i+1,R=n-1;
            while (L<R){
                int curSum=nums[i]+nums[L]+nums[R];
                int curGap=Math.abs(curSum-target);
                if(curGap<gap){
                    gap=curGap;
                    ans=curSum;
                }
                if(curSum==target){
                    return target;
                } else if (curSum<target) {
                    L++;
                }else {
                    R--;
                }
            }
        }

        return ans;
    }
}