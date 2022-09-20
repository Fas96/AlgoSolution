class Solution {
    public int findLength(int[] nums1, int[] nums2) {
         int N = nums1.length;
        int M = nums2.length;
        int mx=0;
        int[][]dp=new int[N+1][M+1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(nums1[i]==nums2[j]) {
                    dp[i+1][j+1] =1 + dp[i][j];
                    mx = Math.max(mx, dp[i+1][j+1]);
                } 

            }
            
        }

        return mx;
    }
      private boolean contigious(List<Integer> num, List<Integer> n2) {
        return Collections.indexOfSubList(n2 , num)!=-1;
    }

}