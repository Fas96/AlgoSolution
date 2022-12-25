class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
         int N=nums.length;
        int M=queries.length;
        
        int ans[] = new int[M];
         Arrays.sort(nums);
        
        for(int i=0;i<M;i++){
            int sum=0;
            int count=0;
            for(int j=0;j<N;j++){
                if(sum+nums[j]<=queries[i]){
                    sum+=nums[j];
                    count++;
                }
            }
            ans[i]=count;
        }
        return ans;
    }
}