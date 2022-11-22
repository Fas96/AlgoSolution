class Solution {
    public boolean isAnagram(String s, String t) {
             int[] sMap= new int[26];

        for (Character c : s.toCharArray()) {
            sMap[c-'a']++;
        }
        for (Character c : t.toCharArray()) {
            sMap[c-'a']--;
        }

        return Arrays.stream(sMap).allMatch(a->a==0);
    }
}