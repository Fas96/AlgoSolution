class Solution {
    public int minimumMoves(String s) {
       
        int nOperations = 0; 
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'X'){ 
                nOperations++;
                i += 2;
            }
            
        }
        return nOperations;
    }
}