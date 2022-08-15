class Solution {
    public int romanToInt(String s) {
   int res = 0;
    Map<Character, Integer> map = new HashMap<Character, Integer>() {{
      put('I', 1);
      put('V', 5);
      put('X', 10);
      put('L', 50);
      put('C', 100);
      put('D', 500);
      put('M', 1000);
    }};
    for (int i = 0; i < s.length(); i++) {
      int curVal = 0;
      if (i + 1 < s.length() && s.charAt(i) == 'I' && (s.charAt(i + 1) == 'V'
          || s.charAt(i + 1) == 'X')) {
        curVal = -1;
      } else if (i + 1 < s.length() && s.charAt(i) == 'X' && (s.charAt(i + 1) == 'L'
          || s.charAt(i + 1) == 'C')) {
        curVal = -10;
      } else if (i + 1 < s.length() && s.charAt(i) == 'C' && (s.charAt(i + 1) == 'D'
          || s.charAt(i + 1) == 'M')) {
        curVal = -100;
      } else {
        curVal = map.get(s.charAt(i));
      }
      res += curVal;
    }
    return res;
    }
}