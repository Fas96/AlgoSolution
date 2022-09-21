class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
          int N=nums.length;
        int[] result= new int[N];
        if(N == 0)
            return new int[0];
        int sum = 0;

        for(int i = 0; i < N; i++) {
            if(nums[i] % 2 == 0) {
                sum += nums[i];
            }
        }
        for(int i = 0; i < queries.length; i++) {
            int val = queries[i][0];
            int index = queries[i][1];
            int x = (val + nums[index]);
            sum -= (nums[index] % 2 == 0) ? nums[index] : 0;
            sum += (x % 2 == 0) ? x : 0;
            nums[index] = x;
            result [i] = sum;
        }


        return result;
    }
}