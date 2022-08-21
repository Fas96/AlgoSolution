class Solution {
    public int numTrees(int n) {
     
        int res = Math.toIntExact(factorialXTwo(n));
        return res;
    }
 long factorialXTwo(int n) {
      long k =1;
        for (int i = 2; i <= n; i++) 
        {
            k = 2*(2*i-1)*k/(i+1);
        }
     return k;
   }
    
//   nCr  =  	n!
//   	 r!(n - r)!

       // comb = factorial(n) / (factorial(r) * factorial(n-r));
}