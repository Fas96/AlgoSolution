class Solution {
    public int lengthOfLongestSubstring(String s) {
     if(s.length()<=1) return s.length();
    int L=0,R=0,maxLen=0,N=s.length();
    char[] arr=s.toCharArray();
    Map<Character,Integer> hm= new HashMap<>();
    while (R<N){
      hm.merge(arr[R],1, (oldValue, newValue) -> oldValue + 1);

      while (hm.size()!=R-L+1){
        hm.merge(arr[L],hm.get(arr[L]),(oldValue, newValue) -> oldValue -1);
        if(hm.get(arr[L])==0)hm.remove(arr[L]);
        L+=1;
      }
      maxLen=Math.max(maxLen,R-L+1);
//      maxLen=Math.max(maxLen,hm.size());
      R++;
    }
   
        return  maxLen;
  }
}