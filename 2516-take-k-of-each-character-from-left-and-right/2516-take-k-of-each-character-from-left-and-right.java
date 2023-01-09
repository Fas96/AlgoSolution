class Solution {
    public int takeCharacters(String str, int k) {
          int ans = Integer.MAX_VALUE, c[] = { 0, 0, 0 };
        for (int i = 0; i < str.length(); i++) c[str.charAt(i) - 'a']++;
        if (c[0] < k || c[1] < k || c[2] < k) return -1;
        for (int s = 0, e = 0; e < str.length(); e++) {
            c[str.charAt(e) - 'a']--;
            while (s <= e && (c[0] < k || c[1] < k || c[2] < k)) c[str.charAt(s++) - 'a']++;
            ans = Math.min(ans, str.length() - (e - s + 1));
        }
        return ans; 
    }
}