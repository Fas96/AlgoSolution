class Solution {
    public long zeroFilledSubarray(int[] nums) {
        int N=nums.length;
        long subZerosCount=0;

        int L=-1;
        for (int i = 0; i < N; i++) {
            if(nums[i]!=0) L=i;
            else subZerosCount+=(i-L);
        }
        return subZerosCount;
    }
    //TLE N*N
//     public long zeroFilledSubarray(int[] nums) {
//     int N=nums.length,L=-1;
//         long subZerosCount=0;
        

//         for (int i = 0; i < N; i++) {
//             if(nums[i]!=0) continue;
//             int L=i;
//             while (L<N && nums[L]==0){
//                 L++;
//                 subZerosCount++;
//             }
//         }

//         return subZerosCount;
//      }
}