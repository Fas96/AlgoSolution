class Solution {
    public boolean isPalindrome(String s) {
                StringBuilder str= new StringBuilder();
        for (char a: s.toCharArray()) {
             if(Character.isLetterOrDigit(a))str.append(Character.toLowerCase(a));
        }
        
      return str.toString().equals(str.reverse().toString()); 
    }
}