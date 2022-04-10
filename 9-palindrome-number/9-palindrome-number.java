class Solution {
    public boolean isPalindrome(int x) {
           String valueOf = String.valueOf(x);
        int bg=0;
        int end=valueOf.length()-1;
        while (bg<end){
            if(valueOf.charAt(bg)!=valueOf.charAt(end) && bg!=end){
                return false;
            }
            bg++;
            end--;
        }
        return true;
    }
}