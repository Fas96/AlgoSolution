class Solution {
    public void reverseString(char[] s) {
  
      int j=0;
            char[] rs= new char[s.length];
            StringBuffer bd= new StringBuffer();
            for (int i = s.length-1; i >-1; i--) {
                rs[j]=s[i];
                bd.append(rs[j]);
                j+=1;
            }
            String s1 = bd.toString();
            for (int i = 0; i < s1.length(); i++) {
                s[i]=s1.charAt(i);
            }
            System.out.println(Arrays.toString(s).toCharArray());   
}
}