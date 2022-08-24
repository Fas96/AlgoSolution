class Solution {
    public boolean isPowerOfThree(int n) {
        return n>0 && help(n);
    }
    
    boolean help(int n){
        while (n % 3 == 0) {
            n /= 3;
        }
        return n == 1;
    }
  
}