class Solution {
    public void reverseString(char[] s) {
  
      int lf = 0;
        int rf = s.length-1;
        while(lf<rf){
            char tmp = s[rf];
            s[rf] = s[lf];
            s[lf] = tmp;
            lf++;
            rf--;
        }
}
}