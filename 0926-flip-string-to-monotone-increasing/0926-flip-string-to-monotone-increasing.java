class Solution {
    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        int flip0 = 0;
        int flip1 = 0;
        for(int i=0;i<n;i++) {
            if (s.charAt(i) == '0') {
                flip0++;
            }
        }
        int res = flip0;
        for(int i=0;i<n;i++) {
            if (s.charAt(i) == '0') {
                flip0--;
            } else {
                flip1++;
            }
            res = Math.min(res, flip0 + flip1);
        }
        return res;
        
    }
     
}