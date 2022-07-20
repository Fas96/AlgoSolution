class Solution {
    public void reverseString(char[] s) {
         helper(0, s);
        for(int i=0;i<r.size();i++){
            s[i]=r.get(i).toCharArray()[0];
        }
    }
    
    
List<String> r=new ArrayList<>();
private  void helper(int index, char [] str) {
  if (str == null || index >= str.length) {
    return;
  }
  helper(index + 1, str);
   r.add(""+str[index]+"");
  }
}
 

