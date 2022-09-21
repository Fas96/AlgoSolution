class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
       int N=nums.length;
        int[] result= new int[N];
        int T= 0;

        for(int i = 0; i < N; i++) {
            if(nums[i] % 2 == 0) {
                T += nums[i];
            }
        }

        for (int i = 0; i < N; i++) {
            int[] quer= queries[i];
            int x=nums[quer[1]]+quer[0];
            T -= (nums[quer[1]] % 2 == 0) ? nums[quer[1]] : 0;
            T += (x % 2 == 0) ? x : 0;
             
            nums[quer[1]] = x;
            result [i] = T;
        }


        return result; 
    }
}
/*
       int N=nums.length;
        int[] result= new int[N];

        for (int i = 0; i < N; i++) {
            int[] quer= queries[i];
            nums[quer[1]]=nums[quer[1]]+quer[0];
          
            result[i]=Arrays.stream(nums).filter(e->e%2==0).sum();
        }


        return result; 
*/