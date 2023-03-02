class Solution {
    public int compress(char[] chars) {
        int N = chars.length;
        int i = 0;
        int j = 0;
        while (i < N) {
            int count = 0;
            char c = chars[i];
            while (i < N && chars[i] == c) {
                i++;
                count++;
            }
            chars[j++] = c;
            if (count > 1) {
                for (char ch : String.valueOf(count).toCharArray()) {
                    chars[j++] = ch;
                }
            }
        }
        return j;
    }
}