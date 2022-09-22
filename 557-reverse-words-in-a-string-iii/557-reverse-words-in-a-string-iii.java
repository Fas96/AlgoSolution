class Solution {
    public String reverseWords(String s) {
          StringBuilder an=new StringBuilder();
        for (String str:s.split(" ")){
            an.append((new StringBuilder(str)).reverse()+" ");
        }
        return an.toString().trim();
    }
}