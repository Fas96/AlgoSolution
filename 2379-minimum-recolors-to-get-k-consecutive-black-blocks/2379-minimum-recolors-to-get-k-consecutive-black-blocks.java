class Solution {
   public int minimumRecolors(String blocks, int k) {
    int s=Integer.MAX_VALUE,count=0;
    if(k>=blocks.length())
      return (int) blocks.chars().filter(c->c=='W').count();

    for (int i = 0; i < blocks.length()-k+1; i++) { 
      s= (int) Math.min(s,blocks.substring(i,k+i).chars().filter(ch->ch=='W').count());
    }
    return s;
}}