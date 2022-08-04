class Solution {
//cp 
 int GCD(int a, int b){
    while(a != 0 && b != 0)
    if (a > b) a %= b;
    else       b %= a;

    return a + b;
  }
    
  public int mirrorReflection(int p, int q) {
    int gcd = GCD(p, q);
    p /= gcd;
    q /= gcd;
    
    return  (q&1) == 1 ? ( (p&1) == 1 ? 1 : 2) : 0;      
  }
  
}