class Solution {
    public String makeGood(String s) {
  while (true) {
         boolean flag = false;
         for (int i = 0; i < s.length() - 1; i++) {
             if (Math.abs(s.charAt(i) - s.charAt(i + 1)) == 32) {
                 s = s.substring(0, i) + s.substring(i + 2);
                 flag = true;
                 break;
             }
         }
         if (!flag) break;
     }
        return s;
    }
}