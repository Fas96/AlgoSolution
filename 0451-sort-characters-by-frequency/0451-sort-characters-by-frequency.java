class Solution {
    public String frequencySort(String s) {
        int[] count = new int[256];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i)]++;
        }
        int[] index = new int[256];
        for (int i = 0; i < 256; i++) {
            index[i] = i;
        }
        for (int i = 0; i < 256; i++) {
            for (int j = i + 1; j < 256; j++) {
                if (count[index[i]] < count[index[j]]) {
                    int temp = index[i];
                    index[i] = index[j];
                    index[j] = temp;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 256; i++) {
            if (count[index[i]] == 0) {
                break;
            }
            for (int j = 0; j < count[index[i]]; j++) {
                sb.append((char) index[i]);
            }
        }
        return sb.toString();
    }
}