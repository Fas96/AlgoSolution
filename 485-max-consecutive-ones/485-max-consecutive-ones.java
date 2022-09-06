class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxLen=Integer.MIN_VALUE;
        int N=nums.length,counter=0;

        for (int i = 0; i < N; i++) {
            if(nums[i]==0){counter=0;}
               if(nums[i]==1){counter++;}
             maxLen=Math.max(counter,maxLen);
            
        }
         

        return maxLen;
    }
}