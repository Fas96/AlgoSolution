class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
           //base case
        List<List<Integer>> res= new ArrayList<>();
        if(nums.length<3)return res;
        Arrays.sort(nums);
        int n=nums.length;

        for (int i = 0; i < n; i++) {
            if(i!=0 && nums[i]==nums[i-1])continue;

            int L=i+1,R=n-1;
            while (L<R){
                int curSum=nums[i]+nums[L]+nums[R];
                if(curSum==0){
                    res.add(Arrays.asList(nums[i],nums[L],nums[R]));
                    L++;
                    R--;
                    //look for unique elements
                    while (L<R && nums[L]==nums[L-1])L++;
                    while (L<R && nums[R]==nums[R+1])R--;
                } else if (curSum<0) {
                    L++;

                }else {
                    R--;
                }
            }
        }

      return res;
    }
}