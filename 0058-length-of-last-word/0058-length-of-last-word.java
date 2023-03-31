class Solution {
    public int lengthOfLastWord(String s) {
        String[] orinalString = s.trim().split(" ");
        int length = orinalString.length;
        return orinalString[length - 1].length();  
    }
}