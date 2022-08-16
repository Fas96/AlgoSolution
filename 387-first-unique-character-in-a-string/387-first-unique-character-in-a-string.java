class Solution {
public int firstUniqChar(String s) {
 
      char[] a = s.toCharArray();
		
		for(int i=0; i<a.length;i++){
			if(s.indexOf(a[i])==s.lastIndexOf(a[i])){return i;}
		}
		return -1;

  }
}