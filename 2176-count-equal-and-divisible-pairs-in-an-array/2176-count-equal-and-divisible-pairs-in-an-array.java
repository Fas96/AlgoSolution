class Solution {
    public int countPairs(int[] nums, int k) {
 int res=0;

        int stat=0;
        int end=nums.length;
        while (stat<end-1){
           int cur= nums[stat];
            int nx=stat+1;
            int nxval=nums[nx];
            while (nx<end){
                if(cur==nums[nx] && ((stat*nx)%k==0))res++;
                nx++;
            }
            stat++;
        }

        return res;
    }
}