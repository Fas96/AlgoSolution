class Solution {
    public int minFlipsMonoIncr(String s) {
         int n = s.length();
        int flip0 = (int) s.chars().filter(c -> c == '0').count();
        if(flip0 == n) return 0;

        int flip1 = 0;
        int res = flip0;

        for(int i=0;i<n;i++) {
            if (s.charAt(i) == '0') flip0--;
            else flip1++;
            res = Math.min(res, flip0 + flip1);
        }
        return res;
        
    }
     
}