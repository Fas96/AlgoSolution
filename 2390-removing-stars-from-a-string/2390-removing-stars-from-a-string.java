class Solution {
    public String removeStars(String s) {
         int n = s.length();
        StringBuilder sb = new StringBuilder();
        sb.append(s.charAt(0));
        
        for (int i = 1; i < n; i++) {
            if(s.charAt(i)=='*')sb.deleteCharAt(sb.length()-1);
            else sb.append(s.charAt(i));
            
        }
        return sb.toString();
    }
}