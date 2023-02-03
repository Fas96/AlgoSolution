class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1) return s;
        StringBuilder[] sb = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            sb[i] = new StringBuilder();
        }
        int i = 0;
        boolean down = true;
        for (char c : s.toCharArray()) {
            sb[i].append(c);
            if(i == 0) down = true;
            if(i == numRows-1) down = false;
            i += down ? 1 : -1;
        }
        StringBuilder res = new StringBuilder();
        for (StringBuilder stringBuilder : sb) {
            res.append(stringBuilder);
        }
        return res.toString();
    }
}