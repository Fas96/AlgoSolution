class Solution {
    public int minDeletionSize(String[] strs) {
       int numColumns = 0;
        for (int i = 0; i < strs[0].length(); i++) { 
            int j = 0;
            while (j < strs.length - 1 && strs[j].charAt(i) <= strs[j + 1].charAt(i)) {
                j++;
            }
            if (j != strs.length - 1) {
                numColumns++;
            }
        }
        return numColumns;
    }
}