class Solution {
    public int removeDuplicates(int[] nums) {
         int L=0,R=1,N= nums.length;
        while (R<N){
            if(nums[L]!=nums[R]){
                L++;
                int t = nums[L];
                nums[L] = nums[R];
                nums[R] = t;
            }
            R++;
        }
        return L+1;
    }
}