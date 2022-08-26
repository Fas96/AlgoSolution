class Solution {
  public boolean reorderedPowerOf2(int n) { 
     int x = 1;
     char[] giveCharArr=(""+n).toCharArray();
     Arrays.sort(giveCharArr); 
      
  for (int i = 1; i < 1000000000; ){
      char[] c = ("" + i).toCharArray();
      Arrays.sort(c);
      
      if((new String(c)).equals(new String(giveCharArr))) return true;
      i <<= 1;
    }
      
    return false;
  }
  
}