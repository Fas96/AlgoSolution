class Solution {
    public String gcdOfStrings(String str1, String str2) {
        
        if(!(str1 + str2).equals(str2 + str1)) return "";
        int n = str1.length();
        int m = str2.length();
        int gcd = gcd(n, m);
        return str1.substring(0, gcd);
    }
    private int gcd(int a, int b) {
        int gcd = 1;
        for (int i = 1; i <= a && i <= b; ++i) {
            if (a % i == 0 && b % i == 0) gcd = i;
        }
        return gcd;
    }
}