class Solution {
    public int minimumMoves(String s) {
       
       int nOperations = 0;
       int idx = 0;
       int N = s.length();
         while (idx < N) {
              if (s.charAt(idx) == 'X') {
                nOperations++;
                idx += 3;
              } else  idx++;
              
         }
        
    return nOperations;
    }
}