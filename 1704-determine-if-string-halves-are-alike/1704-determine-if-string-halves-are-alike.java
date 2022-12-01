class Solution {
    public boolean halvesAreAlike(String s) {
        
     int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(s.charAt(i))) {
                if (i < s.length() / 2) {
                    count++;
                } else {
                    count--;
                }
            }
        }
        return count == 0;
        

    }

    private boolean isVowel(char charAt) {
        return charAt == 'a' || charAt == 'e' || charAt == 'i' || charAt == 'o' || charAt == 'u' || charAt == 'A' || charAt == 'E' || charAt == 'I' || charAt == 'O' || charAt == 'U';
    }
}