class Solution {
    public int numTrees(int n) {
        long k =1;
        for (int i = 2; i <= n; i++) 
        {
            k = 2*(2*i-1)*k/(i+1);
        }
        int res = Math.toIntExact(k);
        return res;
    }
 int factorial(int n) {
      int fact = 1;
      int i = 1;
      while(i <= n) {
         fact *= i;
         i++;
      }
      return fact;
   }
    
// nCr  =  	n!
//   	 r!(n - r)!

       // comb = factorial(n) / (factorial(r) * factorial(n-r));
}