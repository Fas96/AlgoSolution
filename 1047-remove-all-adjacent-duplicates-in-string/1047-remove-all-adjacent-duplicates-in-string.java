class Solution {
    public String removeDuplicates(String s) {
       StringBuilder sb=new StringBuilder();
        for(int i=0;i<s.length();i++){
            if(sb.length()>0&&sb.charAt(sb.length()-1)==s.charAt(i)){
                sb.deleteCharAt(sb.length()-1);
            }else{
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();

    }
}
/*
TLE
 public String removeDuplicates(String s) {
         while (true) {
            boolean flag = false;
            for (int i = 0; i < s.length() - 1; i++) {
                if (s.charAt(i) == s.charAt(i + 1)) {
                    s = s.substring(0, i) + s.substring(i + 2);
                    flag = true;
                    break;
                }
            }
            if (!flag) break;
        }
        return s;
    }
*/
