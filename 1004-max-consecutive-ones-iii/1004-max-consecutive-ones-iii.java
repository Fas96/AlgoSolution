class Solution {
    public int longestOnes(int[] nums, int k) {
        int maxLen=0,N=nums.length,counter=0;
        if(N<2 && 0<k) return N;
        int L=0,R=0;
        while (R<N){
           if(nums[R]==0){counter++;}
           while (k<counter){
               if(nums[L]==0){counter--;}
               L++;
           }
           maxLen=Math.max(maxLen,R-L+1);
         R++;
        }



        return maxLen;
    }
}