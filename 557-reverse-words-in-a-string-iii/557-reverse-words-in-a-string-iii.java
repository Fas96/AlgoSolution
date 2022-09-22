class Solution {
    public String reverseWords(String s) {
          String an="";
        for (String str:s.split(" ")){
            an+=(reverse(str)+" ");
        }
        return an.trim();
    }
private String reverse(String input){
    char[] in = input.toCharArray();
    int begin=0;
    int end=in.length-1;
    char temp;
    while(end>begin){
        temp = in[begin];
        in[begin]=in[end];
        in[end] = temp;
        end--;
        begin++;
    }
    return new String(in);
}
}