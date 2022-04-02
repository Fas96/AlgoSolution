class Solution {
    public boolean validPalindrome(String s) {
           int failIndex = isPalindrome(s);
        if (failIndex == -1)
            return true;

        if (isPalindrome(s.substring(0, failIndex) + s.substring(failIndex + 1)) == -1) {
            return true;
        }
        if (isPalindrome(s.substring(0, s.length() - 1 - failIndex) + s.substring(s.length() - failIndex)) == -1) {
            return true;
        }

        return false;
    }

    /**
     * @param s
     * @return if s is Palindrome String, return -1 else return the index
     */
    private int isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return left;
            }
            left++;
            right--;
        }
        return -1;
    } 
}