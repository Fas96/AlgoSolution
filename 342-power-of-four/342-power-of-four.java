class Solution {
    public boolean isPowerOfFour(int num) {
       return  num > 0 && help(num);
    }
        boolean help(int n){
        while (n % 4 == 0) {
            n /= 4;
        }
        return n == 1;
    }
  
}