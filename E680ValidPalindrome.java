package leetcode;

public class E680ValidPalindrome {
    static  class Solution {
        public  static  boolean validPalindrome(String s) {
            System.out.println();
            if(s.length()>=1  && s.length()<=Math.pow(10,5)){
                for (int i = 0; i < s.length(); i++) {

                    String partofString = (s.substring(0, i) +  s.substring(i + 1)).toLowerCase();

                    StringBuilder sb=new StringBuilder(partofString);
                    sb.reverse();
                    System.out.println(sb+"||"+partofString);
                    if(partofString.equals(sb.toString())){
                        return true;
                    }

                }
            }


            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println(Solution.validPalindrome("hvxvuiewcjxqrfjmrxcnsaaazjnpvwcufatumlhadmahhbfahoohafbhhamdahlmutafucwvpnjzaaasncxrmjfrqxjcweiuvxvh"));
    }
}
