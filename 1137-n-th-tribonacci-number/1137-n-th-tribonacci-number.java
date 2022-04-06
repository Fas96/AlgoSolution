class Solution {
    public int tribonacci(int n) {
             int t0=0,t1=1,t2=1;

            if (n==1  || n==2)return t2;

            int t_n=0;
            for (int i = 3; i < n+1; i++) {
                t_n=t0+t1+t2;
                t0=t1;
                t1=t2;
                t2=t_n;
            }
            return t_n;
    }
}