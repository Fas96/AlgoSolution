class Solution {
public int firstUniqChar(String s) {
 
    int res=-1;
    List<Character> keeper=new ArrayList<>();
    for (int i = 0; i < s.length(); i++) {
      int finalI = i; 
      if (keeper.contains(s.charAt(finalI)))continue;
      long count = s.chars().filter(ch -> ch == s.charAt(finalI)).count();
      if(count==1 && !keeper.contains(s.charAt(finalI))){
        return finalI;
      }else{
        keeper.add(s.charAt(finalI));
      }
    }
    return res;

  }
}