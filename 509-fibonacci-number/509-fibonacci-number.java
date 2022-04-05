class Solution {
    public int fib(int n) {
       int[] list= new int[n+1];
          if(n==0) return 0;
            list[0]=0;
            list[1]=1;
           if(n<1){
                return list[n];
            }
            int st=0;
            int st2=1;
            for (int i = 2; i < n+1; i++) {
                list[i]=st+st2;
                st=st2;
                st2=list[i];
            } 
            return list[n]; 
    }
} 